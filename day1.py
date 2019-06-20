# 2019.6.13 by lixs
# learn link list
# add two numbers

"""
first define a linklist class
personally think this class give some memory to a variable
and variable.next can go to next memory

"""

class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def convertNumToLinkList(self,d):
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        if d==0:
            return ptr
        while d!=0:
            rem = int(d%10)
            ptr.next = ListNode(rem)
            ptr = ptr.next
            d = d//10
        ptr = dummyRoot.next
        return ptr

    def addTwoNumbers(self, l1,l2):
        num1 = 0; num2 = 0
        u_place = 0
        while l1 != None :
            num1 += l1.val*10**u_place
            l1 = l1.next
            u_place += 1
        u_place = 0
        while l2 != None :
            num2 += l2.val*10**u_place
            l2 = l2.next
            u_place += 1
        res = num1 + num2
        d = res
        print(d)
        ptr = self.convertNumToLinkList(d)
        print(ptr)
        return ptr

    def printValInLinkList(self,l):
        tmp = 1
        while l != None:
            print("%s position value is %s" % (tmp, l.val))
            l = l.next
            tmp += 1


if __name__ == "__main__":
    train = Solution()
    l1 = train.convertNumToLinkList(12341234)
    l2 = train.convertNumToLinkList(12341234)
    result = train.addTwoNumbers(l1,l2)
    train.printValInLinkList(result)
