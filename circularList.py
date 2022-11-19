class Empty(Exception):
    """Error attempting to access an element from an empty container.""" 
    pass

class CircularList:
    """List implementation using circularly linked list for storage."""

    #-------------------------- nested Node class --------------------------    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element' , '_next'
        def  __init__(self, element, next):
            self._element = element
            self._next = next
        
    #------------------------------- Circular List methods -------------------------------
    def __init__ (self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__ (self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        head = self._tail._next    
        return head._element 
    
    def first_ref(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        head = self._tail._next    
        return head

    def remove(self):
        """Remove and return first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty( 'queue is empty' )
        oldhead = self._tail._next 
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next #bypass oldhead  
        self._size -= 1
        return oldhead._element
    
    def add_last(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            newest._next = newest # initialize circularly
        else:
            newest._next = self._tail._next # new node points to head
            self._tail._next = newest   # old tail points to new node
        self._tail = newest    # new node becomes the tail
        self._size += 1
        
    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next

    def __str__(self):
        cur_size = 0
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        else:
            s = '' 
            tail =  self._tail
            cur_size = self._size
            while cur_size != 0:
                head = self._tail._next
                s += str(head._element)
                self._tail = self._tail._next
                cur_size -= 1
            self._tail = tail
            return s
        
class check_references(CircularList):
    def check_ref(self,head,node,n):
        
        for i in range(n):
            if node == head:
                return print('Same references from a list')
            node = node._next
        return print('References not same from a list')   

CL = check_references()
for i in range(1,6): CL.add_last(i)
print(CL)
head = CL.first_ref()
node = head._next
n = len(CL)
print(n)
print(head._element)
CL.check_ref(head,node,n)

# different reference 
CL2 = check_references()
for i in range(6,9): CL2.add_last(i)
node2 = (CL2.first_ref())._next 
print(CL2)
print(node2._element)
CL2.check_ref(head,node2,n)      