class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for element in strs:
            if ''.join(sorted(element)) not in res_dict:
                res_dict[''.join(sorted(element))] = []
            res_dict[''.join(sorted(element))].append(element)
        return list(res_dict.values())