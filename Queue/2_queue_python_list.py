class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue."
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue."
        else:
            self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "There is no elemet in the queue."
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None

"""
Time and Space Complexity of Queue 
create queue O(1) O(1)
Enqueue O(n) O(1)
Dequeue O(n) O(1)
Peek O(1) O(1)
isEmpty O(1) O(1)
delete Entire Queue O(1) O(1)
"""