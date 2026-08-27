class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(strs)
        sorted_str = [''.join(sorted(text)) for text in strs]

        anagram_index_map = {}
        for index, text in enumerate(sorted_str):
            if text not in anagram_index_map:
                anagram_index_map[text] = []
            anagram_index_map[text].append(index)

        output_list = []

        for anagram, index_list in anagram_index_map.items():
            anagram_index_list = []
            for index in index_list:
                anagram_index_list.append(strs[index])
            output_list.append(anagram_index_list)
        return output_list

