class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)

        res = []
        prev_cnt, prev_val = 0, None

        while heap:
            c, v = heapq.heappop(heap)
            res.append(v)
            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_val))
            c += 1
            prev_cnt, prev_val = c, v

        return res






