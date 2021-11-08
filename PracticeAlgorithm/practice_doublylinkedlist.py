class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class ManageNode2:
    def __init__(self, data):  # default data를 넣어줌
        self.head = Node(data)
        self.tail = self.head

    def searchFront(self, data):
        if self.head is None:
            print("리스트가 비어있습니다")

        count = 1
        node = self.head
        while node.next:
            if node.data == data:
                print("찾으려 하는 노드는 ", count, "번째에 있습니다.")
            node = node.next
            count = count+1

    def searchBack(self, data):
        if self.tail is None:
            print("리스트가 비어있습니다")

        count = 1
        node = self.tail
        while node.previous:
            if node.data == data:
                print("찾으려 하는 노드는 끝에서", count, "번째에 있습니다.")
            node = node.previous
            count = count+1

    def addNode(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        node = self.head
        while node.next:
            node = node.next

        newNode = Node(data)
        node.next = newNode
        newNode.previous = node  # previous도 지정해줘야해
        self.tail = newNode  # tail이라는 친구에 newNode를 넣는 것

    def insertFront(self, data, inputData):
        if self.head is None:
            self.head = Node(inputData)

        node = self.head
        inputNode = Node(inputData)
        while node.next:
            if node.data == data:
                temp = node.next
                node.next = inputNode
                inputNode.previous = node
                inputNode.next = temp
                inputNode.next.previous = inputNode
            node = node.next
        pass

        if node.data == data:
            node.next = inputNode
            inputNode.previous = node
            self.tail = inputNode

    def insertBack(self, data, inputData):
        if self.tail is None:
            self.tail = Node(inputData)

        node = self.tail
        inputNode = Node(inputData)
        while node.previous:
            if node.data == data:
                temp = node.previous
                node.previous = inputNode
                inputNode.next = node
                inputNode.previous = temp
                inputNode.previous.next = inputNode
            node = node.previous
        pass

        if node.data == data:
            node.previous = inputNode
            inputNode.next = node
            self.head = inputNode

    def printNode(self):
        if self.head is None:
            print("리스트가 비어있습니다.")

        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)


li1 = ManageNode2(1)

print("head 노드는 ", li1.head.data)
print("tail 노드는 ", li1.tail.data)
print("---------------------------")

for i in range(2, 11):
    li1.addNode(i)

print("head 노드는 ", li1.head.data)
print("tail 노드는 ", li1.tail.data)
print("---------------------------")

li1.insertBack(9, 8.5)
li1.insertBack(10, 9.5)
# li1.insertBack(11, 10.5) 당연히 안들어감
li1.insertBack(1, 0.5)
li1.insertFront(1, 1.7)
li1.insertBack(1.7 , 1.3)
li1.insertFront(3, 3.5)
li1.insertFront(10, 10.5)

li1.printNode()
print("head 노드는 ", li1.head.data)
print("tail 노드는 ", li1.tail.data)
print("---------------------------")

li1.searchFront(4)
li1.searchBack(9)
