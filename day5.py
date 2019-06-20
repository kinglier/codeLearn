# 2019.6.18 lixs
#Reverse integer

"""
I finish this requir very fast, but the memery limit problem come out

Finally, I find the best solve method is convert the int to str first
because in str format, we can use the str[::-1] to reverse the str without
complicate operation.
"""

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x > 0:
            save = [1]
        elif x<0:
            save = [-1]
        else:
            return 0

        while x != 0:
            save.append(x%10)
            x = x//10
        for i in range(1,len(save)):
            result = result + save[i]*10**(len(save) -1 -i)
        result = result*save[0]

        return result
    def reverseUseString(self, x):
        x = str(x)
        if (x[0] == '-'):
            I = int(x[0] + x[1:][::-1])
            if(I < (-2**31)):
                return 0
        else:
            I = int(x[::-1])
            if(I > (2**31)-1):
                return 0
        return I
