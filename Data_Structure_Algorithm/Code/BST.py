class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(min_node.data, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")

bst = BST()

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

print("Postorder traversal:")
bst.postorder_traversal()  

print("\n\nHapus node dengan nilai 6")
bst.delete(6)

print("\nPostorder traversal setelah penghapusan:")
bst.postorder_traversal()