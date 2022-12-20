class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result_array = []
        result_array.append(nums[0])
        sum = nums[0]
        
        for i in range(1,len(nums)):
            
            result_array.append(nums[i]+sum)
            sum += nums[i]
            
        
        
        return result_array
            