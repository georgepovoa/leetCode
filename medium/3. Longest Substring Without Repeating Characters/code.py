class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_range = len(set(s))
        for mr in range(max_range,0,-1):
            for j in range(len(s)):
                if len(s[j:j+mr])<mr:
                    break
                elif len(set(s[j:j+mr])) == len(s[j:j+mr]) :
                    return len(s[j:j+mr])
        return 0

 