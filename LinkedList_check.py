class Empty(Exception):
    """Error attempting to access an element from an empty container.""" 
    pass

class LinkedList:
    """Implementation using a singly linked list for adding from head storage."""

    #-------------------------- nested Node class --------------------------    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element' , '_next'
        def  __init__(self, element, next):
            self._element = element
            self._next = None
        
    #------------------------------- List methods -------------------------------
    def __init__ (self):
        """Create an empty List."""
        self._head = None
        self._size = 0

    def __len__ (self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def add_first(self, e):
        """Add element e to the first of the list."""
        newest = self._Node(e, self._head) # create and link a new node 
        newest._next = self._head
        self._head = newest
        self._size += 1       
        
    def remove_first(self):
        """remove element e from the first of the list."""
        if self._head is None:
            raise Empty( 'List is empty' )
        self._head = self._head._next
        self._size -= 1  
     
    def first_ref(self):
        """Return (but do not remove) the ref at the first of the List.
        Raise Empty exception if the List is empty. """
        if self.is_empty():
            raise Empty( 'List is empty' )
        return self._head
    
    def first(self):
        """Return (but do not remove) the element at the first of the List.
        Raise Empty exception if the List is empty. """
        if self.is_empty():
            raise Empty( 'List is empty' )
        return self._head._element  


    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty( 'List is empty' )
        answer = self._head._element  
        self._head = self._head._next
        self._size -= 1
        return answer

    def __str__(self):
        if self.is_empty():
            raise Empty( 'List is empty' )
        else:
            s = '' 
            head =  self._head
            for i in range(self._size):
                s += str(head._element)
                head = head._next
            return s 

class combine(LinkedList):
    
    def combineList(self, L, M):
        _ref = M.first_ref()
        while _ref is not None:
            self.add_first(_ref._element)
            _ref = _ref._next
            
L1 = combine()            
L = combine()
for i in range(3): L.add_first(i) 
M = combine()
for i in range(3,5): M.add_first(i)    
print(L)
#print(M)
L1.combineList(L,M)
print(L1)
