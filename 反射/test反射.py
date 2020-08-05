obj = 10

class Student:
    name = 'abc'

obj = Student()

if hasattr(obj,'name'):
     print("有属性")
     setattr(obj,'age',26)
     print(getattr(obj,'age'))
else:
    print("没有属性")
    setattr(obj,'name',11)