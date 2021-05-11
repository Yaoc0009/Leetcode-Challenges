
# Simple solution based on Sieve of Eratosthenes
# Time Complexity: O(n log log n)
# Space Complexity: O(n)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
            
        arr = [1]*n
        arr[0],arr[1] = 0,0
        
        for i in range(2,int(math.sqrt(n))+1):
            if arr[i] == 1:
                for j in range(i**2,n,i):
                    arr[j] = 0
                    
        return sum(arr)
            
