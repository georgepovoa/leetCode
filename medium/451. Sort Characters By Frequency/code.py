class Solution:
    def frequencySort(self, s: str) -> str:
        dict_of_chars = {}
        result = ""
        
        for i in s:
            if i not in dict_of_chars:
                dict_of_chars[i] = 1
            else:
                dict_of_chars[i] +=1
        
        
        while(dict_of_chars != {}):
            greater_char_until_now = 0
            index_of_greater_value = 0 
            for i in dict_of_chars.items():
                
                if i[1] > greater_char_until_now:
                    greater_char_until_now = i[1]
                    index_of_greater_value = i[0]
            
            for i in range(dict_of_chars[index_of_greater_value]):
                result += index_of_greater_value
                    
            
            del dict_of_chars[index_of_greater_value]
        return result
        