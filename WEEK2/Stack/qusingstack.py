class MyQueue:

    def __init__(self):
        
        self.queue = []

    def push(self, x: int) -> None:
        
        if self.queue == []:
            self.queue.append(x)
        else:
            self.queue.insert(0, x)


    def pop(self) -> int:
        
    
        return self.queue.pop()


    def peek(self) -> int:
        
       
       
        return self.queue[-1]


    def empty(self) -> bool:
        
        return len(self.queue) == 0