#2019.7.10 lixs
#接雨水


"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self,height):
        if len(height) == 0:
            return 0
        cube = 0
        #make a list save the heightest from current position to the right
        right_max = [0 for _ in range(len(height))]
        right_max[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            right_max[i] = max(height[i], right_max[i+1])

        # current cube = min(left_max[i], right_max[i]) - height[i]
        left_max = height[0]
        for i in range(1,len(height)):
            space = min(left_max, right_max[i]) - height[i]
            if space > 0:
                cube = cube + space
            left_max = max(left_max,height[i])
            
        return cube

if __name__ == "__main__":
    train = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = train.trap(height)
    print(result)

