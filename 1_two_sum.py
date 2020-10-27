from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for index, value in enumerate(nums):
        result = target - value
        if result in nums[index + 1:]:
            return [index, nums.index(result, index + 1, len(nums))]
