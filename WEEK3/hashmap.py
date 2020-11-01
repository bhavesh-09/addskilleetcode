class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    



t=HashTable()
t.__setitem__("january 9",1997)
t.__setitem__("january 11",1997)
t.__setitem__("feb 9",1998)



print(t.arr)
print(t.get_hash("january 9"))

print(t.__getitem__("feb 9",1998))

