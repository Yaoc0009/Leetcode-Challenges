class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a = len(word1)
        b = len(word2)
        
        prev_arr, curr_arr = [0]*(b+1),[0]*(b+1)
        
        for i in range(a):
            for j in range(b):
                if word1[i] == word2[j]:
                    curr_arr[j+1] = prev_arr[j] + 1
                else: 
                    curr_arr[j+1] = max(prev_arr[j+1],curr_arr[j])
                
            prev_arr,curr_arr = curr_arr,prev_arr
                    
        return a+b-2*prev_arr[b]
