import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-i for i in target]
        total = sum(target)
        heapq.heapify(heap)
        while heap[0] != -1:
            num = -heapq.heappop(heap)
            total -= num
            if num <= total or total < 1:
                return False
            
            num %= total
            total += num
            heapq.heappush(heap, -num or -total)
            
        return True
