#接收输入信息
print ("How old are you?")
# 接收控制台的输入信息
age = input()
print ("How tall are you?")
height = input()
print("How much do you weight?"),
weight = input()

print ("So,you're %r old, %r tall and %r heavy." %(
    age, height, weight))	




# 读取文件
file_object = open('C:/Users/WWH/Desktop/1.txt','r')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )
print(all_the_text)
