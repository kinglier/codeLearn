# 2019.6.15 lixs
#Median of two sorted Arrays

"""
Firstly, I should say I really know so little things
I write about 40 rows of code while other only use 10 rows to defeat mine

list = lis1 + lis2
list.sort()
then everythin become easy

"""

class Solution:
    def mergeTwoSortedArrays(self,num1,num2):
        len1 = len(num1)
        len2 = len(num2)
        print(len1,len2)
        position1,position2 = 0,0
        num_merge = [0 for i in range(len1+len2-1)]
        for i in range(len1+len2):
            if position1 == len1:
                num_merge[i+1:] = num2[position2:]
                return num_merge
            if position2 == len2:
                num_merge[i+1:] = num1[position1:]
                return num_merge
            print(i)
            print(position1,position2)
            if num1[position1] <= num2[position2]:
                num_merge[i] = num1[position1]
                position1 += 1
            else:
                num_merge[i] = num2[position2]
                position2 += 1
        return num_merge

    def findMedianSortedArrays(self,num1,num2):
        n = len(num1)
        m = len(num2)
        if n ==0 and m ==0:
            print("Erro: both arrays is empety")
            return
        num_merge = self.mergeTwoSortedArrays(num1,num2)
        print(num_merge)
        odd = (n + m)%2
        opp = (n + m)//2
        if odd == 0:
            median = (num_merge[opp-1] + num_merge[opp])/2
        else:
            median = num_merge[opp]
        return median
        print(num_merge)

    def mergeTwoSortedArrays1(self,nums1,nums2):
        lst1 = nums1 + nums2
        lst1.sort()
        if len(lst1) % 2 == 0:
            median = (lst1[int((len(lst1)/2)-1)]+lst1[int(len(lst1)/2)])/2
        else:
            median = lst1[int(len(lst1)//2)]
        return median


if __name__ == "__main__":
    list1 = []
    list2 = []
    train = Solution()
    result = train.mergeTwoSortedArrays1(list1,list2)
    print("The median is %f" % result)
