import time;

# 原始方法
def index(x,y):
    time.sleep(3)
    print(x,y)

#装饰器，不改变原始方法的情况下，增加新的功能
def outer(func):
    def wrapper(*args,**kwargs):
        start = time.time();
        func(*args,**kwargs)
        stop = time.time();
        print(stop-start)
    return wrapper
#偷梁换柱
index = outer(index);


#此时的index函数已经被替换
index(111,222)