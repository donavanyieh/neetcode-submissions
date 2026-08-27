class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 1: Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #                 return [i, j]

        # Method 2: Two pointer
        # Additional layer: We need to keep track of the original index, not just return the elements
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append([num, i])
        sorted_nums = sorted(sorted_nums)
        # Initialize pointer at the start and at the end
        left_p, right_p = 0, len(nums)-1
        while left_p < right_p:
            if sorted_nums[left_p][0] + sorted_nums[right_p][0] == target:
                return sorted([sorted_nums[left_p][1], sorted_nums[right_p][1]])
            elif sorted_nums[left_p][0] + sorted_nums[right_p][0] > target:
                right_p -= 1
            else:
                left_p += 1