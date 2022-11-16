class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack.""" 
        self._data = [ ]
    # nonpublic list instance 
    """Return the number of elements in the stack."""
    def __len__(self): 
        return len(self._data)
     
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e) # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
          Raise Empty exception if the stack is empty. """
        if self.is_empty():
            raise Empty( 'Stack is empty' )
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
          Raise Empty exception if the stack is empty. """
        if self.is_empty():
                raise Empty( 'Stack is empty' )
        return self._data.pop( )

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['               # opening delimiters
    righty = ')}]'              # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)           # push left delimiter on stack
        elif c in righty:
            if S.is_empty( ):
                return False    # nothing to match with
            if righty.index(c) != lefty.index(S.pop( )):
                return False
    return S.is_empty( ) # were all symbols matched?
print(is_matched('[(5+x)-(y+z)]]'))


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find( '<' )
    while j != -1:
        k = raw.find( '>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith( '/' ):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop( ):
                return False
        j = raw.find( '<' , k+1)
    return S.is_empty( )

raw="""<body>
<center>
<h1> The Little Boat </h1>
</center>
</body>"""
print(is_matched_html(raw))


class R2Stack(ArrayStack):
    def _full_pop_r(self, results, counter):
        if self.is_empty():
            return None
        else:
            results[counter] = self.pop()
            counter += 1
            self._full_pop_r(results, counter)
        
    
    
    def full_pop(self): #override the Stack.full_pop method
        results = [None]*len(self)
        counter = 0
        self._full_pop_r(results, counter)
        
        return results


S2 = R2Stack()
for i in range(10):S2.push(i) 
print('S2 =',S2)    
print('removed stack S2:', S2.full_pop()) 
print('S2 =',S2)
