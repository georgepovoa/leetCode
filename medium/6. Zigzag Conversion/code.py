class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        for i in range(numRows):
            result.append([])
        
        current_row = 0
        down= True
        up = False
        for i in range(len(s)):
            result[current_row].append(s[i])
            
            if down:
                if current_row +1 < numRows :
                    current_row +=1 
                if current_row == numRows-1:
                    up = True
                    down = False
                    continue
                    
            if up:
                if current_row -1 >= 0:
                    current_row -=1 
                if current_row == 0:
                    up = False
                    down = True
                    
                
                
        for i in range(len(result)):
            result[i] ="".join(result[i])
        
        result = "".join(result)
                    
                
                
        
        return result
            
            
        