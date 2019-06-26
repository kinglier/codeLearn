#2019.6.15 lixs
#

"""
nums.remove(val)
del val
"""

class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        j = len(nums)-1
        
        if len(nums) == 0:
            return i
        while i != j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i+1

    def removeElement1(self, nums, val: int) -> int:
        nums.sort()
        head = tail = 0
        if nums == []:
            return 0
        for i in range(len(nums)):
            if nums[i] == val:
                print(head,tail)
                print(nums)
                if i == 0:
                    head = 0
                else:
                    if nums[i-1] != val:
                        head = i
                if i == len(nums) -1:
                    tail = len(nums) -1
                    return len(nums)
                elif nums[i+1] != val:
                    tail = i
                    nums = nums[0:head] + nums[tail+1:]
                    print(nums)
                    return len(nums)
        return len(nums)
if __name__ == '__main__':
    train = Solution()
    nums = [0,1,2,2,3,0,4,2]
    result = train.removeElement1(nums,2)
    print(result)
