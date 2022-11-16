class Empty(Exception):
    """Error attempting to access an element from an empty container.""" 
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 4 # moderate capacity for all new queues
    def __init__ (self):
        """Create an empty queue."""
        self._data = [None] *  ArrayQueue.DEFAULT_CAPACITY
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
            return self._data[self. front]
        
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
                     Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) 
        self._size -= 1
        return answer  
    
    
    def enqueue(self, e):
        """Add an element to the back of queue.""" 
        if self._size == len(self._data):
            self._resize(2 *  len(self._data)) # double the array size 
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
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

    def printdemoCQueue(self):
        if(self._size == 0):
            print('No element present in the queue')
        else:
            for i in range(self._size):
                print(self._data[i])

Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)
Q.enqueue(7)
Q.enqueue(1)
Q.enqueue(6)
Q.printdemoCQueue()
len(Q)
Q.dequeue()
Q.enqueue(8)
Q.enqueue(9)
Q.dequeue()