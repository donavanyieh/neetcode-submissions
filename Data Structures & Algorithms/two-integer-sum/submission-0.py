class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_position_map = {}
        
        for i,n in enumerate(nums):
            diff = target - n

            if diff in value_position_map:
                return sorted([i, value_position_map[diff]])
            
            value_position_map[n] = i