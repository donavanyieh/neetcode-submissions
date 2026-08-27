class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}

        for num in nums:
            frequency_dict[num] = 1 + frequency_dict.get(num, 0)

        sorted_frequency_dict = {k: v for k, v in sorted(frequency_dict.items(), key=lambda item: item[1], reverse = True)}
        
        output_list = []
        for count in range(k):
            output_list.append(list(sorted_frequency_dict)[count])
        
        return output_list