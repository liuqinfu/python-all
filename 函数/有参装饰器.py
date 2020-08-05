import time
#假设在调用index函数之前需要根据不同类型采用数据库、文件来验证用户信息
def auth(db_type):
    def desco(func):
        def wrapper(*args,**kwargs):
            if db_type == "file":
                print("基于文件的认证")
            elif db_type == "db":
                print("基于数据库的认证")
            else:
                print("免认证")
            start = time.time()
            res = func(*args,**kwargs)
            stop = time.time()
            print("程序共耗时：%s" % (stop-start))
            return res
        return wrapper
    return desco

@auth(db_type="db")
def index(x,y):
    time.sleep(3)
    print(x,y)


index(1111,2222)

print((lambda x,y:x+y)(1,2))