class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        m=len(strs[0])
        for i in range(len(strs)):
            m =min(len(strs[i]), m)
        
        l=""
        i=0
        while i<m:
            c=strs[0],[i]
            for j in range(1,len(strs)):
                if strs[j][i]!=c:
                    return l
            l=l+c
            i+=1
        return l
s=Solution()
print(s.longestCommonPrefix(["flower","flow","flop"]))


