class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for letter in s:
            result ^= ord(letter)
        for letter in t:
            result ^= ord(letter)
        return chr(result)
        
#Approach2 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for letter in t:
            result += ord(letter)
        for letter in s:
            result -= ord(letter)
        return chr(result) 
