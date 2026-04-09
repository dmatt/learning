class Node():
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None 

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder_print':
            return self.preorder_print(tree.root, "")
        elif traversal_type == 'inorder_print':
            return self.inorder_print(tree.root, "")
        elif traversal_type == 'postorder_print':
            return self.postorder_print(tree.root, "")
        else:
            print('not supported')
            return False

    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += "%s - " % start.label
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += "%s - " % start.label
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += "%s - " % start.label
        return traversal

#             1
#          /     \
#        2          3
#       / \       /   \
#      4   5     6      7

if __name__ == "__main__":
    tree = BinaryTree('1')
    
    tree.root.left = Node('2')
    tree.root.right = Node('3')

    tree.root.left.left = Node('4')
    tree.root.left.right = Node('5')
    tree.root.right.left = Node('6')
    tree.root.right.right = Node('7')

    # print(tree.print_tree("preorder_print"))
    # print(tree.print_tree("inorder_print"))
    print(tree.print_tree("postorder_print"))

# Tree traversal types:
# breadth first
# depth first