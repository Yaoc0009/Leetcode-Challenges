class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if count>1 or (1<i<len(nums)-1 and nums[i]<nums[i-2] and nums[i+1]<nums[i-1]):
                    return False
        
        return True 
