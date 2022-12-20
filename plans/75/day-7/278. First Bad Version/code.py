# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        bot = 0
        top = n
        mid = top // 2 
        while(True):
            if (isBadVersion(mid)):
                top = mid
                mid = (bot+top)//2
            elif (not isBadVersion(mid) and isBadVersion(mid+1) and not isBadVersion(mid-1) ):
                return mid +1
            
            elif (not isBadVersion(mid)):
                bot = mid
                mid = (bot+top) // 2
            
