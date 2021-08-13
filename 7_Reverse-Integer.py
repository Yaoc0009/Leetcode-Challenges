# Brute force
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        rev_s = ''
        if s[0] == '-':
            rev_s += '-'
            s = s[1:]
        for i in reversed(s):
            rev_s += i
            
        if int(rev_s) < -2**31 or int(rev_s) > 2**31 - 1:
            return 0
        else:
            return int(rev_s)
          
