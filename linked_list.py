class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node.next
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

a = Node(6)
b = Node(16)
c = Node(34)
d = Node(67)
e = Node(8)

f = Node(11)
g = Node(5)
h = Node(7)

l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
print(f" Dastlabki holat: {l_list.printList()}")

#PUSH
#
# l_list.push(11)
# l_list.push(69)
# l_list.push(102)
# l_list.push(40)
# l_list.push(98)
# print(f" Keyingi holat: {l_list.printList()}")

#INSERT
# l_list.insert(a, 100)
# l_list.insert(b, 209)
# l_list.insert(c, 980)
# l_list.insert(d, 38)
# l_list.insert(e, 17)
# print(f" Keyingi holat: {l_list.printList()}")

#APPEND
# l_list.append(11)
# l_list.append(99)
# l_list.append(90)
# l_list.append(19)
# l_list.append(33)
# l_list.append(66)
# print(f" Keyingi holat: {l_list.printList()}")
