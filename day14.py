#2019.6.28 lixs
#Search the insert position

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
from typing import List

class Solution:
    def searchInsert(self,nums,target):
        if len(nums) == 0:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                return i
            if nums[i] > target and nums[i-1] < target:
                return i
        return 0

    def searchInsert1(self, nums: List[int], target: int) -> int:
        try:
            for i, num in enumerate(nums):
                if target == num or target < num:
                    return i
            return i+1
        except:
            return 0


if __name__ == "__main__":
    train = Solution()
    digits = [1,3,5,6]
    target = 5
    result = train.searchInsert1(digits,target)
    print(result)

            
