class Solution:
    def reverse(self, x: int) -> int:
        

        is_negative = False
        if x < 0 :
            is_negative = True
            x = x*-1
        
        result = str(x)[::-1]
        
        if is_negative:
            result = int(result)*-1
        
        result = int(result)
        
        if result.bit_length()>=32:
            return 0
        
        
        return result
        
        
            
        