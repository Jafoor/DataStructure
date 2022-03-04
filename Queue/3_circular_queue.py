
from sys import maxsize


class Queue:
    def __init__(self, maxSize) -> None:
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        return False
    
    def isEmpty(self):
        if self.start == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "There is no space to insert."
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The item has been inserted at the end of the queue."
            
    def dequeue(self):
        if self.isEmpty():
            return "There is no elements in the queue."
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == maxsize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is not any elements in the queue."
        else:
            return self.items[self.start]
    

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

q = Queue(5)
print(q.isEmpty())
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q)
q.dequeue()
print(q.peek())
q.delete()
print(q)

"""
Time and Space Complexity
1. Create Queue - O(1) - O(n)
2. Enqueue - O(1) - O(1)
3. Dequeue - O(1) - O(1)
4. Peek - O(1) - O(1)
5. isEmpty - O(1) - O(1)
6. isFull - O(1) - O(1)
7. Delete Entire Queue - O(1) - O(1)
"""