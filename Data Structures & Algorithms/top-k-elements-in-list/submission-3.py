class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Normal sorted method
        # number_freq_map = {}

        # for num in nums:
        #     number_freq_map[num] = 1 + number_freq_map.get(num, 0)

        # sorted_number_freq_map = {k:v for k,v in sorted(number_freq_map.items(), key = lambda item: item[1], reverse = True)}

        # return list(sorted_number_freq_map)[:k]

        # Heap
        number_freq_map = {}
        for num in nums:
            number_freq_map[num] = 1 + number_freq_map.get(num, 0)
        
        heap = []
        for num, freq in number_freq_map.items():
            heapq.heappush(heap, (-freq, num)) # simulate maxheap

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res