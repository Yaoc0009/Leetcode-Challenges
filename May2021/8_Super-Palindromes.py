import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        right = int(right)
        left = int(left)
        count = 0
        lim = 10**9
        
        # odd length palindrome
        for i in range(lim):
            i = str(i)
            num = i + i[-2::-1]
            num_sq = int(num)**2
            if num_sq > right:
                break
            if num_sq >= left and self.isPalindrome(num_sq):
                count += 1
                
        # even length palindrome
        for i in range(lim):
            i = str(i)
            num = i + i[::-1]
            num_sq = int(num)**2
            if num_sq > right:
                break
            if num_sq >= left and self.isPalindrome(num_sq):
                count += 1
                                
        return count
    
    def isPalindrome(self,s):
        s = str(s)
        n = len(s)
        
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True
        
        
