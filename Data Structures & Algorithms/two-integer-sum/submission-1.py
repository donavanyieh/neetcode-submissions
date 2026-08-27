class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Using two pointer on sorted array
        # p1 = 0
        # p2 = 1

        # nums_sorted = sorted(nums)
        # while p2 <= len(nums_sorted)-1:
        #     sums = nums_sorted[p1] + nums_sorted[p2]
        #     if sums == target:
        #         return [p1, p2]
            
        #     elif sums < target:
        #         p2 += 1

        #     elif sums > target:
        #         p1 += 1

        # Using hashmap 2 pass
        # val_index_map = {}

        # for index, value in enumerate(nums):
        #     val_index_map[value] = index

        # for index, value in enumerate(nums):
        #     diff = target - value
        #     if diff in val_index_map and val_index_map[diff]!=index:
        #         return [index, val_index_map[diff]]

        # Using hashmap 1 pass
        val_index_map = {}
        for index,val in enumerate(nums):
            if index == 0:
                val_index_map[val] = index
            else:
                diff = target - val
                
                if diff in val_index_map:
                    return [val_index_map[diff], index]
                
                val_index_map[val] = index
