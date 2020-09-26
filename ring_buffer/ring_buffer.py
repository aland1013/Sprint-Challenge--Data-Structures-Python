class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = None

    def append(self, item):
        length = len(self.storage)
        
        if length == 0:
            self.storage.append(item)
            self.oldest = 0
        
        elif length < self.capacity:
            self.storage.append(item)
        
        else:
            self.storage[self.oldest] = item
            if self.oldest < self.capacity - 1:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        return self.storage