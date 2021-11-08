import random

# random 함수
a = int(random.random() * 10)
b = int(random.uniform(10, 20))
c = random.randint(10, 20)
d = random.choice("Hello Alice")
e = random.randrange(2,20,3)
print(a, b, c, d, e)

str = "            helllllllllllo             "
print(str)
print(str.strip())
print(str.strip("o"))
str = str.strip('l')
str = str.replace("l","")
print(str)

text = ",,,,,123.....water....pp"
print(text.lstrip(',123.p'))
print(text.rstrip(',123.p'))
print(text.strip(',123.p'))

dict = {1: "hi", 2:"me"}
print(dict.get(1))