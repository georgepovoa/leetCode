# Ideal Solution
# not made by myself
# Alone

# https://www.youtube.com/watch?v=Y0lT9Fck7qI
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1 
        two = 1
        for i in range(n-1):
            temp = one
            one = one+ two
            two = temp
        return one
                

print(Solution.climbStairs(Solution,38))
                