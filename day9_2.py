#2019.6.22 lixs
#Merge Two Sorted Lists



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        head = l
        while True:
            if l1 == None:
                    l.next = l2
                    return head.next
            if l2 == None:
                    l.next = l1
                    return head.next   
            if l1.val <= l2.val:   
                l.next = l1
                l = l.next
              
                l1=l1.next
                if l1 == None:
                    l.next = l2
                    return head.next         
            else:
                l.next = l2
                l = l.next
              
                l2=l2.next
    
