class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] # list to store items
        self.oldest = None # pointer to oldest item

    def append(self, item):
        length = len(self.storage)
        
        # list is empty
        if length == 0:
            self.storage.append(item)
            self.oldest = 0
        
        # list is not empty but has room for a new item
        elif length < self.capacity:
            self.storage.append(item)
        
        # list is at capacity
        else:
            self.storage[self.oldest] = item
            if self.oldest < self.capacity - 1:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        return self.storage