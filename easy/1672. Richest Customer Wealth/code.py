class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in accounts:
            max_value = 0
            for j in i:
                max_value += j 
            
            if max_value > richest:
                richest = max_value
        
        return richest