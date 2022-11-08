class Vector:
    """Represent a vector in a multidimensional space."""
    def  __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] *  d
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
    def   __getitem__(self, j):
        """Return jth coordinate of vector.""" 
        return self._coords[j]
    def    __setitem__(self, j, val):
        """Set jth coordinate of vector to given value"""
        self._coords[j] = val
    def  __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            # relies on     len     method
            raise ValueError( 'dimensions must agree' )
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    # start with vector of zeros

    def __radd__(self,other):
        if len(self) != len(other):
            # relies on     len     method
            raise ValueError( 'dimensions must agree' )
        result = Vector(len(self)) 
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def  __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    def    __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other   # rely on existing   __eq__     definition
    def str (self):
        """Produce string representation of vector."""
        return '<'+ str(self._coords)[1:-1] + '>' # adapt list representation
    def __mul__(self,other=3):
        result = Vector(len(self)) 
        for j in range(len(self)):
            result[j] = self[j] * other
        return result    

if __name__ == '__main__':
    v = Vector(5)
    print(v._coords)
    v[1] = 2
    v[-1] = 4
    print(v._coords)
    u= v.__mul__(5)
    print(u._coords)
    total = 0
    for entry in v:
        total += entry
    print(total) 