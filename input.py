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




from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())
# txt.close()#处理完文件后将他关闭
# print txt.read()#测试是否关闭了


print("Type the  filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())
