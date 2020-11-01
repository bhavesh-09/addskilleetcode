class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_str=len(s)
        p_str=len(p)
        if s_str < p_str:
            return []
        
        p_co=Counter(p)
        s_co=Counter()
        result=[]
        
        for i in range(s_str):
            s_co[s[i]] +=1 
            if i >= p_str:
                if s_co[s[i-p_str]]==1:
                    del s_co[s[i-p_str]]
                else:
                    s_co[s[i-p_str]]-=1
                
            if p_co==s_co:
                result.append(i - p_str + 1)
                
                  
            
        return result