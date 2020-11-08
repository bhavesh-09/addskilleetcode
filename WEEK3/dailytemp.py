class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result, s = [0] * len(T), []
        for i in range(len(T)):
            while s and T[s[-1]] < T[i]:
                result[s.pop()] = i - s[-1]
            s.append(i)
        return result 
        