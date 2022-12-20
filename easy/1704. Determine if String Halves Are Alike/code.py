class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        size = int(len(s)/2)
        
        half_1 = 0
        half_2= 0
        
        for i in s[0:(size)]:
            if i in vowels:
                half_1 +=1
        
        for i in s[size::] :
            if i in vowels:
                half_2+=1
        
        if half_2 == half_1:
            return True
        else:
            return False
        
        