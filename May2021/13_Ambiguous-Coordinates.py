class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        coords = []
        s = s[1:-1]
        
        for comma in range(1,len(s)):
            left,right = s[:comma],s[comma:]
            
            left_list = self.getNumber(left)
            right_list = self.getNumber(right)
            
            if left_list and right_list:
                [coords.append("(" + x + ", " + y + ")") for x in left_list for y in right_list]
            
        return coords
    
    def getNumber(self,num):
        arr = list()
        
        if num[0] != '0' or len(num)==1:
            arr.append(num)
        
        for dec_pt in range(1,len(num)):
            whole, dec = num[:dec_pt],num[dec_pt:]
            
            if (whole[0] == '0' and len(whole) > 1) or dec[-1] == '0':
                continue
            arr.append(whole + '.' + dec)
                   
        return arr
