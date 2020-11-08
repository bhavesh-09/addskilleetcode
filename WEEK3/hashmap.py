class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
    

    def __getitem__(self,index):
        h=self.get_hash(index)
        self.arr[h]
        

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for i,element in enumerate(self.arr[h]) : 
            if len(element)==2 and element[0]==key:
                self.arr[h][i]=(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))
    def  __delitem__(self,key):
        h=self.get_hash(key)
        for index ,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]



t=HashTable()
# t.__setitem__("january 9",1997)
# t.__setitem__("january 11",1997)
t["feb 9"]=1998
t["march 9"]=1997
t["feb 9"]=1999





# print(t.get_hash("feb 9"))
del t["march 9"]
print(t.arr)

# print(t.__getitem__("feb 9"))


