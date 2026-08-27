class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_val_map = {}

        for item in strs:
            sorted_str = "".join(sorted(item))
            if sorted_str not in sorted_str_val_map:
                sorted_str_val_map[sorted_str] = []
            sorted_str_val_map[sorted_str].append(item)

        print(sorted_str_val_map)
        return list(sorted_str_val_map.values())