import re
phonenum=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo =phonenum.search('My number is 415-666-6262.')
print('Phone number found:'+mo.group())
