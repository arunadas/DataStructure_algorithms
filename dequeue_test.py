class Empty(Exception):
    """Error attempting to access an element from an empty container.""" 
    pass

class ArrayDeque:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 5 # moderate capacity for all new queues
    def __init__ (self):
        """Create an empty queue."""
        self._data = [None] *  ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
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
            return self._data[self._front]
        
    def last(self):
        """Return (but do not remove) the element at the front of the queue.
          Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty( 'Queue is empty' ) 
            return self._data[-1]
        
    def delete_first(self):
        """Remove and return the first element of the queue (i.e., FIFO).
                     Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) 
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:   #shrinking underlying array reduce array size 
            self._resize(len(self._data) // 2)     #to half when elements stored is short of 1/4 of capacity
        return answer 
    
    def delete_last(self):
        """Remove and return the first element of the queue (i.e., FIFO).
                     Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        answer = self._data[-1]
        self._data[-1] = None 
        self._size -= 1    #to half when elements stored is short of 1/4 of capacity
        return answer
    
    
    def add_last(self, e):
        """Add an element to the back of queue.""" 
        if self._size == len(self._data):
            self._resize(2 *  len(self._data)) # double the array size 
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def add_first(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 *  len(self._data)) # double the array size
        old = self._data
        self._data = [None] * len(old)
        self._data[0] = e
        walk = self._front
        for k in range(1,self._size+1):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0    
        self._size += 1 
        
    def  _resize(self, cap): # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        
    def __str__(self):
        result = []
        if(self._size == 0):
            print('No element present in the queue')
        else:
            result = (dq._data)
        return str(result)    
           
        
dq =  ArrayDeque()
dq.add_last(9)
dq.add_last(1)
print(dq)
dq.add_first(5)
print(dq)
dq.add_last(4)
dq.add_last(2)
dq.add_first(3)
# print(len(dq))
print(dq._data)
print(dq)