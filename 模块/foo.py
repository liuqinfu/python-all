print("foo.py")
#控制被其他地方以*的方式导入时，引用过多不需要的东西
__all__=['x','func1']
x=1
def func1():
    print("func1")

def func2(x):
    print("func2")