#2019.7.1 lixs
#Maximum Subarray

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


class Solution {
    public int maxSubArray(int[] nums) {

        if(nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];

        int []dp = new int[nums.length];
        int head = 0;
        dp[0] = nums[0];

        for(int i = 1; i < nums.length; i++){
            dp[i] = Math.max(dp[i-1] + nums[i], nums[i]); //核心代码
            if(dp[i-1] + nums[i] < nums[i])
                head = i;
        }

        int max = dp[0]; //找最大和
        for(int i = 0; i < dp.length; i++){
            if(max < dp[i])
                max = dp[i];
        }

        return max;

    }
}

