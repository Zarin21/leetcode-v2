class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = Counter(nums)
        heap = []
        for num, freq in num_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for freq, num in heap:
            result.append(num)
        return result