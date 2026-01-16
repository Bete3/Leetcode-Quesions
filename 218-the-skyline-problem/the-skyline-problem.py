class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        res = []
        heap = [(0, float('inf'))]
        prev = 0

        for x, neg_h, r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_h:
                heapq.heappush(heap, (neg_h, r))
            cur = -heap[0][0]
            if cur != prev:
                res.append([x, cur])
                prev = cur

        return res