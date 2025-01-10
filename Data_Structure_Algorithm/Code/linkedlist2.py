class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node =self.head
        nodes = []
        while node is not None :
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
        
coba1 = LinkedList()

coba1.add_first(Node("Asik"))
print(coba1)

coba1.add_first(Node("SDA"))
print(coba1)

coba1.add_first(Node("Praktikum"))
print(coba1)