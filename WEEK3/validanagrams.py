class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)


s=Solution()
print(s.isAnagram(s="anagram",t="nagaram"))