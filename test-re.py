import re
#找出所有的整数和小数
src="wfsfs123dsfds1.23ssdfsfffdsa154dadad2"
l = re.findall("\d+\.?\d*", src)
print(l)
