# '''使用%来格式化'''
# name=input("请输入你的名字");
# 格式化输出  %
# print("驶入的名字为:%s ;哈哈" %(name));
# 格式化输出  传入字典
# name = "柳钦夫";
# age = "26";
# print("我的名字是%(name)s;我的年龄是%(age)s" %{"age":age,"name":name});
# '''使用str.format'''
# str = "我的名字是 {};我的年龄是{}".format("丁雨",25);
# print(str);
# str="我的名字是 {name};我的年龄是{age}".format(age=26,name="张三");
# print(str)
# '''
# f''
# '''
# str = f'我的名字是{name},年龄是{age}';
# print(str)
#
# # 效率： f''> format > %
#
# name =None;
# if not name:
#     print("name 是None %s"%(name));

s = {1,2,3}
print(type(s))

dicts ={"1":"123","2":"344"}
for k in dicts:print(k)