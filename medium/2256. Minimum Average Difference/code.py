class Solution:
    def minimumAverageDifference(self, nums) -> int:
       
        left_side = 0
        right_side = sum(nums)
        
        left_counter = 0
        right_counter = len(nums)
        
        best_result = 10**20
        best_index = -1
        
        for i in nums:
            left_side +=i
            left_counter +=1
            
            right_side -= i
            right_counter -=1
            
            if right_counter == 0 :
                right_counter =1
            
            check = abs( (left_side // left_counter) - right_side // right_counter )
            
            if check < best_result :
                best_result = check
                best_index = left_counter -1
        
        return best_index
            # [2,5,3,9,5,3] = 3

# [0] = 0

# [4,2,0]

# nums = [2,5,3,9,5,3]
# print(Solution.minimumAverageDifference(Solution,nums=nums))

nums = [0]
print(Solution.minimumAverageDifference(Solution,nums=nums))

# nums = [4,2,0]
# print(Solution.minimumAverageDifference(Solution,nums=nums))