str1="hello world "
str2="python hello world "
print("str1[0]:",str1[0])
print("str2[0:5]:",str2[0:5])
l=str1.__len__()
print("更新字符串:",str1+str2)
str3=str1+str2
print(str3)
print(str3.find(str2))
print(str3.count('h'))
print(str1.capitalize())
print(str1.center(50,'+'))

str = "字符串函数";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))
