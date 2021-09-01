'''
The number of ways to get to nth step is equal to the number of ways to get to (n-1)th step plus number of ways to get to (n-2)th step.

ways[n] = ways[n-1] +ways[n-2]

Also, base case at step 0 is 1, since there is 1 way to get to the 0th step. From this, there is also only 1 way to get to 1st step. Hence,

ways[0] = 1 and ways[1] = 1

From the 2 above information, you can get:

ways[2] = ways[1] + ways[0] = 2
ways[3] = ways[2] + ways[1] = 3

and so on...
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one += two
            two = tmp
        return one
