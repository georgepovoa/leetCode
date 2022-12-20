class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        dict_of_index_value = {}
        index_of_mat = 0
        for index, i in enumerate(mat) :
            temp_soldier = 0 
            for j in i :
                if j == 1 :
                    temp_soldier +=1
                dict_of_index_value[index] = temp_soldier     
                
                
        lista_sorteada = sorted(dict_of_index_value, key =dict_of_index_value.get)
        return lista_sorteada[0:k]