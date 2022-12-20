class Solution:
    def longestPalindrome(self, s: str) -> int:
        have_odd = False
        if len(s)<3:
            return len(s)
            
        total = 0
        dct = {}
        
        for I in s:
            if I not in dct :
                dct[I] = 1
            else:
                dct[I] +=1
       
        print(dct)
        for I in dct.values():
            if I %2 !=0:
                have_odd = True
           
            if I >=2:
                total += I // 2
        
        if have_odd:
            return total * 2 +1
        else:
            return total *2

# 12
s="tattarrattat"
print(Solution.longestPalindrome(Solution,s=s))

# 4
s = "aaaa"
print(Solution.longestPalindrome(Solution,s=s))

#2
s = "bb"
print(Solution.longestPalindrome(Solution,s=s))


# 7
s = "abccccdd"
print(Solution.longestPalindrome(Solution,s=s))

s = "AB"
# 1

## can't comprehend AB

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {} # Hash Table   
        ans = []   # every word's frequency 
        odd= 0     # store an odd number's frequency 
        for word in s:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        for times in count.values():
            ans.append(times)
            if times % 2 != 0:
                odd += 1      # calculate an odd number's frequency
        if odd != 0:
            return sum(ans) - odd + 1        
        elif odd == 0:
            return sum(ans) - odd
        
