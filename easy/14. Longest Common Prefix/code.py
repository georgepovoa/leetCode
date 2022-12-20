def longestCommonPrefix( strs) -> str:
    prefix = ""
    try:
        for i in range(len(strs[0])):
            #print("current letter")
            current_letter = strs[0][i]
            #print(current_letter)
            #print("i",i)

            for j in range(len(strs)):
    #                if strs[j][i] != current_letter:
                #print(" J ",j , " I ",i)
                #print("strs[j][i]")
                #print(strs[j][i])
                if strs[j][i] != current_letter:
                    return prefix
            
            prefix += current_letter
            #print(prefix)
        
        return prefix
    except:
        return prefix
    

    

print(longestCommonPrefix(["flower","flower","flower","flower"]))

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]

print(longestCommonPrefix(strs))

strs = ["ab", "a"]

print(longestCommonPrefix(strs))





