class Solution:
    def isNumber(self, s: str) -> bool:
        
        if "inf" in s or "Inf" in s:
            return False
        
        try:
            float(s)          
        except:
            return False
        
        return True
