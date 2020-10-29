class Solution:
    def insert(self, intervals, newInterval):
        i=0
        newarr=[]
        # intervals=[[[1,3],[6,9]]
        # newInterval=[2,5]

        while i<len(intervals) and newInterval[0] > intervals[i][0]:
            # newarr=[[1,3]]
            newarr.append(intervals[i])
            i+=1
        if not newarr or newarr[-1][1] < newInterval[0]:
            newarr.append(newInterval)
        else:
            newarr[-1][1]=max(newarr[-1][1],newInterval[1])
        
        while i<len(intervals):
            if newarr[-1][1]<intervals[i][0]:
                newarr.append(intervals[i])
            else:
                newarr[-1][1]=max(newarr[-1][1],intervals[i][1])
            i+=1
        return(newarr)


s=Solution()
print(s.insert(intervals=[],newInterval=[2,5]))

