""" Return whether the object has an attribute with the given name. """

# hasattr 함수는 첫번째 인자로 object 를 받고 두번째 인자로 attribute name 을 받는다.
# hasattr 는 인자로 들어온 객체가 두번째 인자로 들어온 속성이름을 가지고 있는지 아닌지 확인하는 함수이다.


class Student:
    name = "flouie"
    age = 18
    gender = "Male"


# Student 객체가 name 을 가지고 있으므로 True
print(hasattr(Student, 'name'))

# Student 객체가 grade 을 가지고 있지않으므로 False
print(hasattr(Student, 'grade'))
