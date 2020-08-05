
#只有继承了type类的类才是元类
class Mymeta(type):

    def __init__(self,class_name,class_bases,class_namespace):
        print('runing...')
        print(self)
        print(class_name)
        print(class_bases)
        print(class_namespace)
        print(self.__bases__)
        if not str.istitle(class_name):
            raise NameError('类型必须大写开头')
        if '__doc__' not in class_namespace:
            raise TypeError('必须有文档注释')

    def __new__(cls, *args, **kwargs):
        print('Mymeta new')
        print(cls)
        print(args)
        print(kwargs)
        # 造Mymeta对象
        args=(args[0],(),args[2])
        print(args)
        return super().__new__(cls,*args, **kwargs)


class People(object,metaclass=Mymeta):
    '''
    这是文档注释
    '''
    def __init__(self):
        print('People runing')

# 产生People这个类的过程：People=Mymeta('People',(object,),{...})
# 调用Mymeta发生三件事
# 1先造一个空对象 People,调用类内的__new__方法
# 2调用Mymeta这个类内的__init__方法，完成初始化对象的操作
# 3 返回初始化好的对象


