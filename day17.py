#2019.7.4 lixs
#

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #Jiu Zhang suanfa version. Better use 'while start+1 < end' Condition

        if not nums:
            return -1


        l = 0
        r = len(nums)-1

        if nums[l] == target:return l
        if nums[r] == target:return r

        while l+1<r:
            mid = (l+r)//2
            print(l,mid,r)
            print("========")
            if nums[mid] == target:
                return mid

            if nums[mid]<=nums[r]:
                if target > nums[mid] and target<=nums[r]:
                    l = mid
                else:
                    r = mid
            elif nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid
        return -1

     def search1(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            if nums[mid] <= nums[r]:
                if target > nums[mid] and target <=nums[r]:
                    l = mid
                else:
                    r = mid
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid
        return -1
            



if __name__ == "__main__":
    train = Solution()
    target = 3
    nums = [1,2,3,4]
    result = train.search(nums,target)
    print(result)
