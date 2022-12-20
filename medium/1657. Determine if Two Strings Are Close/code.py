
def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    diferences = 0
    index_of_difs = []
    index = 0
    for i,j in zip(word1, word2):
        print(i,j)
        if i!=j:
            index_of_difs.append(index)
            diferences +=1
        index+=1

    if diferences >2:
        print(index_of_difs)

    else :
        return True    
    return False


print(closeStrings("abc","bca"))

print(closeStrings("cabbba","abbccc"))
    
        
        