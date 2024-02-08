class Stack:

    def __init__(self, items = [], limit = -1):
        self.items = items
        self.limit = limit
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if (self.limit == -1) or len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None    

    def pop(self):
        if len(self.items)>0:
            return self.items.pop()

    def peek(self):
        return self.items

    def size(self):
        return len(self.items)

    def full(self):        
        if len(self.items) >= self.limit:
            return True
        else:
            return False    

    def search(self, target):
        index = len(self.items)-1        
        for item in self.items:
            if item == target:
                return index
            index -=1    
        return -1
