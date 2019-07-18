#2019.7.18 lixs
#合并区间

"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping

"""

class Solution:
    def mergeIntervals(self,nums):
        if len(nums) <=1: return nums
        nums.sort()
        result = [nums[0]]
        for i in range(len(nums)):
            if nums[i][0] <= result[-1][1]:
                result[-1][1] = max(nums[i][1],result[-1][1])
            else:
                result.append(nums[i])

        return result

if __name__ == "__main__":
    train = Solution()
    nums = [[1,3],[2,6],[8,10],[15,18]]
    result = train.mergeIntervals(nums)
    print(result)
