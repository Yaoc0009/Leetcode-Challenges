class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_arr = []
        
        if x < 0:
            return False
        elif x == 0:
            return True
        while int(x) > 0:
            num_arr.append(int(x % 10))
            x /= 10
        for i in range(len(num_arr)//2):
            if num_arr[i] != num_arr[len(num_arr) - 1 - i]:
                return False
            
        return True
