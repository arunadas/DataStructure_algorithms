class _Node:
    def __init__(self, element):
        self._left = None
        self._right = None
        self._element = element

class BTree:
    def __init__(self):
        self._root = None
        self._size = 0
        
    def __len__(self):
        return self._size

    def getRoot(self):
        return self._root

    def add(self, element):
        if self._root is None:
            self._root = _Node(element)
        else:
            self._add(element, self._root)
        self._size += 1    

    def _add(self, element, node):
        if element < node._element:
            if node._left is not None:
                self._add(element, node._left)
            else:
                node._left = _Node(element)
        else:
            if node._right is not None:
                self._add(element, node._right)
            else:
                node._right = _Node(element)
                

    def find(self, element):
        if self._root is not None:
            return self._find(element, self._root)
        else:
            return None

    def _find(self, element, node):
        if element == node._element:
            return node
        elif (element < node._element and node.l is not None):
            return self._find(element, node._left)
        elif (element > node._element and node._right is not None):
            return self._find(element, node._right)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self._root = None

    def printTree(self):
        if self._root is not None:
            self._printTree(self._root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node._left)
            print(str(node._element) + ' ')
            self._printTree(node._right)

root = BTree()
root.add(27)
root.add(14)
root.add(35)
root.add(10)
root.add(19)
root.add(31)
root.add(42) 
root.printTree()
len(root)         