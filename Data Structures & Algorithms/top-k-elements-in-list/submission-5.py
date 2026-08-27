class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        freq_dict_sorted = sorted(freq_dict)

        res_list = []
        for num,count in freq_dict.items():
            res_list.append([count,num])
        res_list = sorted(res_list, reverse = True)
        return [pair[1] for pair in res_list[:k]]


