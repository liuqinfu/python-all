x=0
def fun1():
    x=1
    def func2():
        x=3
        def func3():
            nonlocal x
            x = 2
            print(x)
        func3()
        print(x)
    func2()
    print(x)

fun1()
print(x)