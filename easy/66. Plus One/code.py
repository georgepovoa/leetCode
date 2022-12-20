class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string = str(digits).replace(", ","")
        string = string.replace("[","")
        string = string.replace("]","")
        
        string = int(string) +1
        result = []
        for i in str(string):
            result.append(i)
        return result
        