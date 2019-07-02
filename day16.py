#2019.7.2 lixs
# DP

class Solution:
    def isMatch(self,s,p):
        if len(p) == 0: return len(s) == 0

        first = (len(s)!=0 and s[0] in [p[0],'.'])

        if len(p) >=2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or first and self.isMatch(s[1:],p)

        else:
            return (first and self.isMatch(s[1:],p[1:]))



if __name__ == "__main__":
    train = Solution()
    s = 'ab'
    p = '.*'
    print(len(p))
    print(train.isMatch(s,p))


