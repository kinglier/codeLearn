#2019.6.21 lixs
# 3 SUM


class Solution:

    def threeSum(self,nums):
        result = []
        if len(nums) < 3: return result
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for d in range(j+1,len(nums)):
                        Sum = nums[i] + nums[j] + nums[d]
                        if Sum == 0:
                            arr = [nums[i],nums[j],nums[d]]
                            print(arr)
                            arr.sort()
                            print(arr)
                            if arr not in result:
                                result.append(arr)
        return result

    def threeSum1(self,nums):
        result = []
        numc = []
        if len(nums) < 3: return result
        nums_lib = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] not in nums_lib:
                nums_lib[nums[i]] = 1
                numc.append(nums[i])
            else:
                nums_lib[nums[i]] += 1
        print(nums_lib)
        if 0 in nums_lib and nums_lib[0] >= 3:
            result.append([0,0,0])
        for i in range(len(numc)):
            if (0-numc[i])/2 in nums_lib and nums_lib[(0-numc[i])/2] >=2:
                print([numc[i],-numc[i]/2,-numc[i]/2])
                result.append([numc[i],-numc[i]/2,-numc[i]/2])
        l = len(numc)-1
        for r in range(len(numc)):
            if numc[r] < 0:
                while numc[l] > 0:
                    if -(numc[r] + numc[l]) in numc:
                        result.append([numc[r],-(numc[r] + numc[l]),numc[l]])
                    print(l,r,numc[l])
                    l = l-1
        return result


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,4]
    train = Solution()
    result = train.threeSum1(nums)
    print(result)
