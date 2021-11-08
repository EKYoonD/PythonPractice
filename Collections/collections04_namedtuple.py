# namedtuple()

aa = ("홍길동", 24, "남")
print(aa)

bb = ("윤은경", 26, "여")
print(bb[0])

for n in [aa, bb]:
    print('%s은 %d살인 %s이다.' % (n))

import collections

Person = collections.namedtuple("P", "name age gender")
aa = Person(age=24, name="윤지창", gender="남")
bb = Person(name="윤은경", age=26, gender="여")

for n in [aa, bb]:
    print("%s는(은) %d세인 %s이다" %n)

# OrderedDict : 자료의 순서를 기억하는 사전형 클래스
dic = {}
dic['서울'] = 'seoul'
dic['경기'] = "kyeonggi"
dic['인천'] = "incheon"

for i, j in dic.items():
    print(i, "는 ", j)

# 입력한 순서 기억
dic1 = collections.OrderedDict()

dic1['인천'] = 'incheon'
dic1['서울'] = "seoul"
dic1['경기'] = 'kyeonggi'

for i, j in dic1.items():
    print(i, " = ", j)

dic3 = {}
dic3['서울'] = 'seoul'
dic3['경기'] = "kyeonggi"
dic3['인천'] = "incheon"

dic4 = {}
dic4['인천'] = "incheon"
dic4['서울'] = 'seoul'
dic4['경기'] = "kyeonggi"

print(dic3 == dic4)

dic5 = collections.OrderedDict()
dic5['서울'] = 'seoul'
dic5['경기'] = "kyeonggi"
dic5['인천'] = "incheon"

dic6 = collections.OrderedDict()
dic6['인천'] = "incheon"
dic6['서울'] = 'seoul'
dic6['경기'] = "kyeonggi"

for i, j in dic6.items():
    print(i, j, sep = " : ")

print(dic5==dic6)
str1 = "aaabbbbb"
str2 = "bbbbbcccc"
str3 = str1 + str2
print(str3)