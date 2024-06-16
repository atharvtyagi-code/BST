class Node:
    def __init__(self, key):
        self.value = key
        self.right = None
        self.left = None

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert_left(self, parent, key):
        parent.left = self.insert_data(parent.left, key)

    def insert_right(self, parent, key):
        parent.right = self.insert_data(parent.right, key)
        
    def insert_data(self, root, key):
        if root == None:
            return Node(key)
        
        if root.value > key:
            root.left = self.insert_data(root.left, key)

        elif root.value < key:
            root.right = self.insert_data(root.right, key)


        else:
            return root
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)
        
BST = Binary_search_tree()

BST.root = Node(key=8)
BST.insert_left(parent=BST.root, key = 5)
BST.insert_right(parent=BST.root, key = 13)

BST.inorder(BST.root)

BST.insert_left(BST.root, 2)
BST.insert_right(BST.root, 3)
BST.insert_left(BST.root, 10)
BST.insert_right(BST.root, 15)

BST.inorder(BST.root)