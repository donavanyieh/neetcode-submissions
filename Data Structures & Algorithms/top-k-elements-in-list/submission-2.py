class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_freq_map = {}

        for num in nums:
            number_freq_map[num] = 1 + number_freq_map.get(num, 0)

        sorted_number_freq_map = {k:v for k,v in sorted(number_freq_map.items(), key = lambda item: item[1], reverse = True)}

        return list(sorted_number_freq_map)[:k]