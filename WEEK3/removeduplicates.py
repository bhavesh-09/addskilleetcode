class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        mylist=Counter(A[0])
        for str in A[1:]:
            mylist &=Counter(str)
        return(list(mylist.elements()))

s=Solution()
print(s.commonChars(["bella","label","roller"])
