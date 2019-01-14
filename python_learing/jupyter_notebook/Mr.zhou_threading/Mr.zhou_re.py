import re

# 匹配一行文字中所有的开头字母

s = 'i love you but you don\'t love me'

# \b\w findall

content = re.findall(r'\b\w', s)
#print(content)

# 匹配一行文字中所有数字开头的内容
s1 = '1i1 22love 33you 44but you 66don\'t 77love 8me8'
num = re.findall(r'\b\d', s1)
# print(num)

# 匹配只含有数字和字母的行
s2 = 'i love you  \n 222kkkkk \n adasd \n o12u3123ji\n 123asdad\n 1234awasd'
content = re.findall(r'\w+', s2, re.M)
#print(content)

# 写一个正则表达式,使其能匹配以下字母 'bit', 'bat', 'but', 'hat', 'hit', 'hut'

s3 = "'bit', 'bat', 'but', 'hat', 'hit', 'hut'"
# content = re.findall(r'..t', s3)
# print(content)

s4 = 'se3333 1996-01-06 22:54:34 asdasdasd 2019-01-04 09:44:23'
# content = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', s4)
# print(content)

# 提取电子邮件格式
s5 = """xxxxx@163.com xasdaad asdasd@qq.com ajuoiu123 asiu323@gmail.com"""
# content = re.findall(r'\w+@\w+.com', s5)
# print(content)

# 把以上合法的电子邮件替换成自己的电子邮件
# content = re.sub(r'\w+@\w+.com', '1064201288@qq.com', s5)
# print(content)

# 使用正则提取字符串的单词
s6 = 'i love you not because who 233 of asdaa23 not'
content = re.findall(r'\b[a-zA-Z]+\b', s6)
print(content)
