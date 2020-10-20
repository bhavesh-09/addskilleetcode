class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for i in s:
            if i.isalnum():
                result+=i.lower()
        n=len(result)
        l=0
        r=n-1
        while l<r:
            if result[l] != result [r]:
                return False
            l+=1
            r-=1
        return True