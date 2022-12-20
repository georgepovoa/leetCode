class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote =list(ransomNote)
        magazine = list(magazine)
        

        while (len(ransomNote)>0):
            print(ransomNote)
            if ransomNote[0] in magazine:
                magazine.remove(ransomNote[0])
                ransomNote.remove(ransomNote[0])
                
            else:
                return False
        
        return True