# Brute force
# Alone

class Solution:
    total = 0
    recursivo = 0
    def climbStairs(self, n: int) -> int:
        import time
        
        
        def recursive_increment (x,increment,recursivo):
            
            x += increment
            time.sleep(0.5)
            print("------------------------------")
            print("x,increment",x,increment)
            print(self.total,"total")
            print("recursivo" , recursivo)
            print("------------------------------")
            if x == n : 
                self.total +=1
                return 
            elif x > n:
                return 
            elif x < n :
                self.recursivo +=1
                recursive_increment(x,1,self.recursivo)
                self.recursivo +=1
                recursive_increment(x,2,self.recursivo)
                
        self.recursivo +=1 
        recursive_increment(0,1,self.recursivo)
        
        self.recursivo +=1
        recursive_increment(0,2,self.recursivo)
        
        return self.total
                

print(Solution.climbStairs(Solution,3))
                