"""
Init signature: reversed(self, /, *args, **kwargs)
Docstring:
reversed(sequence) -> reverse iterator over values of the sequence

Return a reverse iterator
"""
# reversed()는 iterable 객체를 역방향으로 전환시킨 reverseiterator 객체를 반환
# 해당 객체가 매직 메소드 __reversed__()를 구현하고 있거나, sequence protocol(__len__() 메소드, __getitem__() 메소드)을 지원하고 있어야 한다
data = list(range(5))
reversed_data = reversed(data)

print(list(reversed_data))

# 아래는 함수의 원형(C 코드 - https://github.com/python/cpython/blob/3.6/Objects/enumobject.c#L244)

"""
static PyObject *
reversed_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Py_ssize_t n;
    PyObject *seq, *reversed_meth;
    reversedobject *ro;
    _Py_IDENTIFIER(__reversed__);

    if (type == &PyReversed_Type && !_PyArg_NoKeywords("reversed()", kwds))
        return NULL;

    if (!PyArg_UnpackTuple(args, "reversed", 1, 1, &seq) )
        return NULL;

    reversed_meth = _PyObject_LookupSpecial(seq, &PyId___reversed__);
    #  해당 객체의 __reversed__() 호출

    if (reversed_meth == Py_None) {
        # __reversed__()가 없다면
        Py_DECREF(reversed_meth);
        # void Py_DECREF(PyObject *o)를 호출해 해당 reversed_math의 reference count를 낮춤
        PyErr_Format(PyExc_TypeError,
                     "'%.200s' object is not reversible",
                     Py_TYPE(seq)->tp_name);
        return NULL;
    }
    if (reversed_meth != NULL) {
        PyObject *res = PyObject_CallFunctionObjArgs(reversed_meth, NULL);
        Py_DECREF(reversed_meth);
        return res;
    }
    else if (PyErr_Occurred())
        return NULL;

    if (!PySequence_Check(seq)) {
        PyErr_Format(PyExc_TypeError,
                     "'%.200s' object is not reversible",
                     Py_TYPE(seq)->tp_name);
        return NULL;
    }

    n = PySequence_Size(seq);
    # sequence 객체의 사이즈
    if (n == -1)
        return NULL;

    ro = (reversedobject *)type->tp_alloc(type, 0);
    # 해당 타입으로 메모리 동적할당
    if (ro == NULL)
        return NULL;

    ro->index = n-1;
    # 인덱스를 n-1(마지막 인덱스)로 변경
    Py_INCREF(seq);
    # reference count 증가
    ro->seq = seq;
    # sequence 객체 할당
    return (PyObject *)ro;
}
"""
