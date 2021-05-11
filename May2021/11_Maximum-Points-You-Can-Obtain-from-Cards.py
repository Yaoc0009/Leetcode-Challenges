class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)
        win_len = len(cardPoints) -k
        
        min_cumsum = cumsum = sum(cardPoints[:win_len])
        
        for i in range(k):
            cumsum += cardPoints[i+win_len] - cardPoints[i]
            if cumsum < min_cumsum:
                min_cumsum = cumsum
                
        return total_sum - min_cumsum
