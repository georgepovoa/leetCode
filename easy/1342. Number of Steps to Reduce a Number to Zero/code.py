class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_count = 0
        
        while(True):
            if num == 0:
                return step_count
            
            if num%2==0:
                num = num/2
                step_count+=1
            else:
                num -=1
                step_count +=1
            
            
        