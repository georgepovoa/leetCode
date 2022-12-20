class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, i in enumerate(nums):
            if index > 0 and i == nums[index-1]:
                continue

            right_pointer = len(nums) - 1
            left_pointer = index+1
            while left_pointer < right_pointer:
                check = i + nums[left_pointer] + nums[right_pointer]
                if check > 0:
                    right_pointer -= 1
                elif check < 0:

                    left_pointer += 1
                else:


                    result.append([i, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    while (nums[left_pointer] == nums[left_pointer-1]) and left_pointer < right_pointer:
                        left_pointer += 1
        return result