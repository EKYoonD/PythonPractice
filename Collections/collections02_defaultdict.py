import collections


def default_value_func():
    return "default_value"

new = "insert value"

dic = collections.defaultdict(default_value_func)
dic2 = collections.defaultdict(str)

print(dic)
dic['n1'] = 35
print(dic["n1"])
print(dic['n2'])
print(dic)

print(dic2['n2'])
print(dic2)
dic2['n1'] = 20
print(dic2)
