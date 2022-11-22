class Node:
    def __init__(self, element):
        self._left = None
        self._right = None
        self._element = element
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
 
    def insert(self, e):
        """Compare the new value with the parent node"""
        if self._element:
            if e < self._element:
                if self._left is None:
                    self._left = Node(e)
                else:
                    self._left.insert(e)
            elif e > self._element:
                if self._right is None:
                    self._right = Node(e)
                else:
                    self._right.insert(e)
        else:
            self._element
        self._size += 1
        
    # Print the tree
    def PrintTree(self):
        if self._left is not None:
            self._left.PrintTree()
        print (self._element),
        if self._right is not None:
            self._right.PrintTree()   
            
            
class countLeft(Node):
    def countLeft(self,root):
        result = []
        if root is not None:
            result = self.countLeft(root._left)
            if self._size is not 0:
                result.append(root._element)
        return result        
    
root = countLeft(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.PrintTree()
root.countLeft(root)