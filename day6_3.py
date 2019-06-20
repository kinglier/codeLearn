#lixs
#


class Solution:
    def cacuBox(self, i, j, ai, aj):
        if ai < aj:
            height = ai
        else:
            height = aj
        box = height*(j-i)
        return box

    def maxArea(self, height):
        result = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                print(i,j,height[i],height[j])
                box = self.cacuBox(i,j,height[i],height[j])
                print(box)
                if box > result:
                    result = box
                print(result)
        return result

class Solution1:
    def maxArea(self, height):
        max_container = 0
        container = height
        while len(container) >= 2:
            print(container)
            print(len(container)-1,min(container[0],container[-1]))
            box = (len(container)-1) * min(container[0],container[-1])
            print(container[0],container[-1])
            if container[0] > container[-1]:
                container.pop(-1)
            else:
                container.pop()
            if box > max_container:
                max_container = box
        return max_container

if __name__ == "__main__":
    lis = [1,8,6,2,5,4,8,3,7]
    train = Solution1()
    result = train.maxArea(lis)
    print(result)
