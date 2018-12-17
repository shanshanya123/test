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
# 1.raw_input()是接受控制台输入的任何信息
# 2.在print后面加“,”可以让输入在同一



# 读取文件
file_object = open('C:/Users/WWH/Desktop/1.txt','r')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )
print(all_the_text)
