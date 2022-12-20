class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}
        
        for index,i in enumerate(s) :
            if i not in s_dict:
                s_dict[i] = [1,[index]]
            else :
                s_dict[i][0] +=1
                s_dict[i][1].append(index)
                
 
        for index,i in enumerate(t) :
            if i not in t_dict:
                t_dict[i] = [1,[index]]
            else :
                t_dict[i][0] +=1
                t_dict[i][1].append(index)
        
        
        
        if len(t_dict) != len(s_dict):
            return False
        else:
            for (vt,kt), (vs,ks) in zip(t_dict.items(),s_dict.items()):
                print(ks,kt)
                if ks != kt:
                    return False
            return True