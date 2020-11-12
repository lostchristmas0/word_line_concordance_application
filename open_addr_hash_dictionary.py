"""
File: open_addr_hash_table.py

"""
from entry import Entry

class OpenAddrHashDict(object):
    "Represents a hash table."""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 8,
                 hashFunction = hash,
                 linear = True):
        self._table = [OpenAddrHashDict.EMPTY] * capacity
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        if key in self:
            return self._table[self._actualIndex].getValue()
        else:
            return None 

    def __delitem__(self, key):
        """Removes the entry associated with key."""
        if key in self:
            self._table[self._actualIndex] = OpenAddrHashDict.DELETED
            self._size -= 1

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        entry = Entry(key, value)
        if key in self:
            self._table[self._actualIndex] = entry
        else:
            self._table[self._actualIndex] = entry
            self._size += 1
            
    def __contains__(self, key):
        """Return True if key is in the dictionary; return
           False otherwise"""
        entry = Entry(key, None)
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(key)) % len(self._table)
        rehashAttempt = 0
        index = self._homeIndex

        # Stop searching when an empty cell is encountered
        while rehashAttempt < len(self._table):
            self._probeCount += 1
            if self._table[index] == OpenAddrHashDict.EMPTY:
                self._actualIndex = index
                return False
            elif self._table[index] == entry:
                self._actualIndex = index
                return True
            
            # Increment the index and wrap around to first 
            # position if necessary
            rehashAttempt += 1
            if self._linear:
                index = (self._homeIndex + rehashAttempt) % len(self._table)
            else:
                # Quadratic probing
                index = (self._homeIndex + (rehashAttempt ** 2+ rehashAttempt) // 2) % len(self._table)

        # An empty cell is found, so store the item
        return False

    def __len__(self):
        return self._size

    def __str__(self):
        resultStr = "{"
        for item in self._table:
            if not item in (OpenAddrHashDict.EMPTY,OpenAddrHashDict.DELETED):
                resultStr = resultStr + " " + str(item)
        return resultStr + " }"

    def __iter__(self):
        """Iterates over the keys of the dictionary"""
        pass

    def homeIndex(self):
        return self._homeIndex

    def probeCount(self):
        return self._probeCount

    def loadFactor(self):
        return len(self._table)/self._size
        
        
def main():
    """Uses an example data set from Chapter 19."""
    table = OpenAddrHashDict(8, lambda x : x)
    for item in (range(10, 71, 10)):
        table[item] = ""
        print( "item:", item, "Home:", table.homeIndex(), "Probes:", table.probeCount(), \
              "Load factor:", table.loadFactor())
        print( table)
    table[2] = ""
    print( "item:", item, "Home:", table.homeIndex(), "Probes:", table.probeCount(), \
          "Load factor:", table.loadFactor())
    print( table)
    return table

if __name__ == "__main__": t = main()

        



