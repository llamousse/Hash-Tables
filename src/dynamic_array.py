class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0 # Count is how much is currently used
        self.capacity = capacity # How much is currently allocated
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            # TODO: resize
            print("Error, array is full")
            return
        
        # Shift everyting to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        
        # Insert our value
        self.storage[index] = value
        self.count += 1
    
    def append(self. value):
        self.insert(self.count, value)
    
    def resize(self):
        