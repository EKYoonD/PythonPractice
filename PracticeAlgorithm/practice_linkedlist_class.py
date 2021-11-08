class Node:
    def __init__(self, data, next=None):  # Node 생성자
        self.data = data
        self.next = next


class NodeManage:
    def __init__(self, data):  # Node 관리하는 NodeManage의 생성자자
        self.head = Node(data)  # 일단 맨 앞에 있는 head를 생성하면서 LinkedList Class 시작

    def addNode(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def printNode(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)

    def deleteNode(self, data):

        if self.head == "":  # 노드가 아예 비어있을 때
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:  # 첫노드에서 값을 찾았을 때
            temp = self.head
            self.head = self.head.next
            del temp

        else:  # 위 두가지 경우 아니면 head 넣고 시작
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next.next
                    node.next.next = None
                    node.next = temp
                node = node.next

    def insertNode(self, data, inputData):
        if self.head is None:  # 노드가 아예 비어있을 때
            print("해당 노드가 없습니다")
            return

        node = self.head
        inputNode = Node(inputData)
        while node.next:
            if node.data == data:
                temp = node.next
                node.next = inputNode
                inputNode.next = temp
            node = node.next

        if node.data == data:  #
            node.next = Node(inputData)

    def search(self, data):

        if self.head is None:
            print("찾는 노드가 없습니다.")

        count = 1
        node = self.head
        while node.next:

            if node.data == data:
                print("찾으려고 하는 데이터가 ", count, "번째 노드에 있습니다.")
            node = node.next
            count = count + 1


l1 = NodeManage(1)

for i in range(2, 11):
    l1.addNode(i)

l1.printNode()
print()

l1.deleteNode(1)
l1.deleteNode(4)
l1.printNode()
print()

l1.insertNode(1, 1.5)
l1.insertNode(3, 3.5)
l1.insertNode(6, 6.5)
l1.insertNode(2, 2.5)
l1.insertNode(10, 10.5)
l1.insertNode(10.5, 11)
l1.printNode()

l1.search(5)
