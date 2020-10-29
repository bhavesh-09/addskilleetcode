class MinStack:

    def __init__(self):
        self.s=[]
        self.minS=[]
        self.size=0
        
       


    def push(self, x: int) -> None:
        if self.size==0:
            self.minS.append(x)
        else:
            if x <= self.minS[-1]:
                self.minS.append(x)
        self.s.append(x)
        self.size+=1
        
        

    def pop(self)->None:
        item=self.s.pop()
        self.size-=1
        if item==self.minS[-1]:
            self.minS.pop()
        
     
    def top(self) ->int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]
    
        
        


