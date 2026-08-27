class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # method 1: anagrams as keys
        res_dict = defaultdict(list)
        for element in strs:
            res_dict[''.join(sorted(element))].append(element)
        return list(res_dict.values())

        # method 2: hash table
        # res = defaultdict(list)
        # print(res)