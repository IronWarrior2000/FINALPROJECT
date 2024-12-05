class Node:
    def __init__(self, value = None, next = None, previous = None):
        self._value_ = value
        self._next_ = next
        self._previous_ = previous
        return
    
    def set(self, value):
        self._value_ = value

    def get_value(self):
        # Return the value of this node
        return self.__value__
    
    def get_next(self):
        # Return this node's next node
        return self.__next__
    
    def get_previous(self):
        # Return this node's previous node
        return self.__previous__
    
    def set_next(self, next):
        # Set this node's next node
        self.__next__ = next
        # Return this node
        return
    
    def set_previous(self, previous):
        # Set this node's previous node
        self.__previous__ = previous
        # Return this node
        return