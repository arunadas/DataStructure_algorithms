class Tree:

    class _Node:
        def __init__(self, element):
            self._left = None
            self._right = None
            self._element = element
            
        
    def __len__(self):
        return self._size 



    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, e):
        """Compare the new value with the parent node"""
        if self._root is None:
            self._root = self._Node(e)
        if self._root._element:
            if e < self._root._element:
                if self._root._left is None:
                    self._root._left = self._Node(e)
                else:
                    self._root._left.insert(e)
            elif e > self._root._element:
                if self._root._right is None:
                    self._root._right = self._Node(e)
                else:
                    self.insert(e)
        else:
            self._root._element
        self._size += 1
        
    # Print the tree
    def printTree(self):
        if self._root._left is not None:
            self._root._left.printTree()
        print ( self._root._element)
        if self._root._right is not None:
            self._root._right.printTree()  
            
            
T = Tree()
T.insert(12)
T.insert(6)
T.insert(14)
T.insert(3)

#T.printTree()



# class Node2:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key 
 
# def insert(root, key):
#     if root is None:
#         return Node2(key)
#     else:
#         if root.val == key:
#             return root
#         elif root.val < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     return root

# def printTree2(root):
#         if root.left:
#             printTree2(root)
#         print ( root.val)
#         if root.right:
#             printTree2(root) 


# root = Node2(12)
# insert(root,6)
# insert(root,14)
# insert(root,3)
# printTree2(root)

