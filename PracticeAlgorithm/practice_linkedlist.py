# LinkedList

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node(0)

# 가장 앞 노드가 뭔지
head = node1


def add(data):  # Linked
    node = head  # node라는 변수에 head를 넣는다
    while node.next:  # node.next가 true (있으면)
        node = node.next  # 다음 노드를 넣는다
    node.next = Node(data)


def insert(data, insertData):
    newNode = Node(insertData)
    node = head
    while node.next:
        if node.data == data:
            temp = node.next
            node.next = newNode
            newNode.next = temp
        node = node.next


def delete(data):
    node = head
    while node.next:
        if node.next.data == data:
            node.next = node.next.next
        node = node.next


def printNodes():  # LinkedList 모두 출력하는 함수
    node = head
    while node.next:
        print(node.data)
        node = node.next
    print(node.data)


for index in range(1, 12):
    add(index)

insert(1, 1.5)
delete(4)

printNodes()
