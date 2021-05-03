import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
              
        # implement max_heap
        max_heap = []
        current_t = 0
        
        for t, end in sorted(courses, key = lambda end: end[1]):
            current_t += t
            heapq.heappush(max_heap, -t)
            if current_t > end:
                current_t += heapq.heappop(max_heap)
                
        return len(max_heap)
            
