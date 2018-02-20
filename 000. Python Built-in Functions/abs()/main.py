""" Return the absolute value of the argument. """

# abs 함수는 인자로 전달된 숫자의 절댓값을 반환하는 함수 이다.
# 인자의 타입에 따라 달라지는데

# 1. <class 'int'> 의 경우, 절댓값을 반환한다.
print(abs(8))
print(abs(-2))

# 2. <class 'float'> 의 경우에도 절댓값을 반환한다.
print(abs(5.666))
print(abs(-3.18))

# 3. <class 'complex'> (복소수)의 경우, 복소수가 복소평면의 원점과 떨어진 거리를 반환한다.
# 여기서 복소평면 이란, x축이 실수축이고 y축이 허수축인 평면을 말한다.
# (파이썬에서 복소수는 i 가 아닌 j로 나타낸다)
print(abs(6j))
print(abs(-2j))
print(abs(1+1j))


# 아래는 abs 함수의 원형 C 코드이다

# 먼저, 인자의 타입이 float 일 때
"""
static PyObject *
float_abs(PyFloatObject *v)
{
    # C 언어의 fabs 함수로 값을 넘겨 계산한다 
    return PyFloat_FromDouble(fabs(v->ob_fval));
}
"""

# 이번에는 인자의 타입이 int 일 때 이다
"""
static PyObject *
long_abs(PyLongObject *v)
{
    if (Py_SIZE(v) < 0)
        # 값이 0보다 작으면(음수이면) long_neg 로 넘긴다
        return long_neg(v);
    else
        # 값이 0보다 크면(양수이면) long_long 으로 넘긴다
        return long_long((PyObject *)v);
}

# 음수 일때
static PyObject *
long_neg(PyLongObject *v)
{
    PyLongObject *z;
    if (Py_ABS(Py_SIZE(v)) <= 1)
        return PyLong_FromLong(-MEDIUM_VALUE(v));
    # 객체를 복사
    z = (PyLongObject *)_PyLong_Copy(v);
    if (z != NULL)
        # 절댓값을 리턴해야 하므로 복사한 객체의 부호를 반전한 후 리턴한다.
        Py_SIZE(z) = -(Py_SIZE(v));
    return (PyObject *)z;
}

# 양수 일때
static PyObject *
long_long(PyObject *v)
{
    if (PyLong_CheckExact(v))
        Py_INCREF(v);
    else
        # 객체를 복사하여 그대로 리턴한다
        v = _PyLong_Copy((PyLongObject *)v);
    return v;
}
"""

# 마지막으로 인자의 타입이 complex 일때 이다
"""
double
_Py_c_abs(Py_complex z)
{
    double result;
    
    # 복소수의 실수부나 허수부가 무한소수일 경우
    if (!Py_IS_FINITE(z.real) || !Py_IS_FINITE(z.imag)) {
        
        # 유효한 무한소수이면 C언의 함수인 fabs 로 절댓값을 구한 후, 리턴한다
        if (Py_IS_INFINITY(z.real)) {
            result = fabs(z.real);
            errno = 0;
            return result;
        }
        if (Py_IS_INFINITY(z.imag)) {
            result = fabs(z.imag);
            errno = 0;
            return result;
        }
   
        return Py_NAN;
    }
    
    # 유한소수일 경우, 복소평면에서 원점과 복소수가 떨어진 거리(빗변)를 반환한다
    result = hypot(z.real, z.imag);
    if (!Py_IS_FINITE(result))
        errno = ERANGE;
    else
        errno = 0;
    return result;
}
"""
