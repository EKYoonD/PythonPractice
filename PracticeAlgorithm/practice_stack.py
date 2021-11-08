# 재귀함수 또한 Stack과 비슷한 모습
def recursive(data):
    if data < 0:
        print("none")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)


recursive(10)

# stack으로 만들어보기

data_stack = list()

data_stack.append("hello")
data_stack.append("python")

print(data_stack.pop())
print(len(data_stack))

data_stack2 = list()


def push(data):
    data_stack2.append(data)


def pop():
    num = data_stack2[-1]
    del data_stack2[-1]
    print(num)


for i in range(10):
    push(i)

print(data_stack2)

pop()
