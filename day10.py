#2019.6.24 lixs
#Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self,nums):
        nums_len = 0
        curr_num = None
        for i in range(len(nums)):
            tmp = nums.pop()
            if tmp != curr_num:
                nums_len = nums_len + 1
                curr_num = tmp
        return nums_len
    def removeDuplicates_(self,nums):
        i = 0
        j = 1
        if len(nums) == 0:
            return i
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i+1
                
if __name__ == "__main__":
    train = Solution()
#    nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = train.removeDuplicates_(nums)
    print(result)
