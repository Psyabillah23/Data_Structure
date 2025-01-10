class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Contoh penggunaan:
dll = DoubleLinkedList()
dll.insert_at_beginning('vania')
dll.display()
dll.insert_at_beginning('dewi')
dll.insert_at_end('dewi')
dll.display()
dll.insert_at_beginning(24)
dll.insert_at_end(30)
print("Isi DLL setelah beberapa insert:")
dll.display()

dll.delete(30)
print("Isi DLL setelah menghapus elemen dengan nilai 30:")
dll.display()
