class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [amount + 1] * (amount + 1)
        count[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    count[i] = min(count[i], count[i - coin] + 1)
        if count[-1] < amount + 1:
            return count[-1] 
        else:
            return -1
