def isSubsequence(s: str, t: str) -> bool:

    last_found = 0
    indexs = []
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j] and j>=last_found :
                last_found = j
                indexs.append(j)
                t = t.replace(t[j],'',1)
                print(t)
                break
    indexs_sorted = sorted(indexs)

    print(indexs_sorted,indexs)
    if len(indexs)<len(s):
        return False
    if indexs_sorted == indexs:
        return True
    else:
        return False

print(isSubsequence("ab","baab"))