'''三个参数：
    file:文件路径、
    mode：对文件的操作模式（r：读、w：写、a：追加）、
    encoding：默认使用操作系统自己的编码
'''
file1 = open("a.txt", "rt");
content = file1.read();
print(content)
'''释放文件在操作系统内存中占用'''
file1.close();

'''使用with上下文，不需要手动关闭文件流'''
with open("a.txt", mode="rt") as f1, open("b.txt", mode="rt") as f2:
    content1 = f1.read();
    content2 = f2.read();
    print(content1)
    print(content2)

with open("c.txt","w+t",encoding="utf-8") as f3:
    print(f3.read())

dicts={1:2,"3":4}

print(dicts[1])