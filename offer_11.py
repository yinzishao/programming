# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
链表中倒数第k个结点
题目描述
输入一个链表，输出该链表中倒数第k个结点。
特殊情况 k=0    k 超过长度  head 为空
"""

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        pre,aft=head,head
        if head ==None:
            return head
        if k ==0:
            return None

        for i in range(k-1):
            if aft.next == None:
                return None
            aft = aft.next
        while aft.next != None:
            aft = aft.next
            pre = pre.next
        return pre