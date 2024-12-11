class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, object):
        self.queue.append(object)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop()
        else:
            return None
    
    def peekQueue(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            return None