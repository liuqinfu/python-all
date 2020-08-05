# class People:
#     def say(self):
#         print("say method")
#
#     def setName(self,name:str)->None:
#         self.name = name
#
#     def getname(self):
#         print(self.name)
#
# people = People()
# people.say()
# people.setName('柳钦夫')
# people.getname()
#
# # People也是一个对象 People是什么类型呢？  type就是元类
# print(type(People))

# 类的三大特征：
# 1 类型
class_name = "People"
# 2 类的基类
class_bases = (object,)
# 3 执行类体代码拿到类的名称空间
class_namespace = {}
class_body = '''
def say(self):
    print("say method")

def setName(self,name:str)->None:
    self.name = name

def getname(self):
    print(self.name)

'''

exec(class_body,{},class_namespace)
print(class_namespace)
# 4 调用元类
t = type(class_name, class_bases, class_namespace)
print(t)
print(t.__dict__)
