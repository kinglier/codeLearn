#2019.6.19 lixs
# int Roman

"""
A very interesting problem
I sovle this problem with a very thump method
there must be simple way which need shorter time comsumption
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        special = {'4':'IV','9':'IX',
                   '40':'XL','90':'XC',
                   '400':'CD','900':'CM'
                  }
        if str(num) in special:
            return special[str(num)]
        unit = {'1':'I','5':'V','10':'X','50':'L','100':'C','500':'D','1000':'M'}
        num = str(num)
        for i in range(len(num)):
            mid = int(num[i])
            if mid == 9:
                result = result + special[str(9*10**(len(num)-1-i))]
                continue
            if mid == 4:
                result = result + special[str(4*10**(len(num)-1-i))]
                continue
            if mid >= 5:
                result = result + unit[str(5*10**(len(num)-1-i))]
                mid = mid-5
            for j in range(mid):
                print(len(num),i)
                result = result + unit[str(10**(len(num)-1-i))]
        return result


if __name__ == "__main__":
    num = 1994
    train = Solution()
    result = train.intToRoman(num)
    print(result)
