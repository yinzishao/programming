# -*- coding:utf-8 -*-
"""

题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 ==None:
            return pHead1
        if pHead1.val < pHead2.val:
            pMerge = pHead1
            pMerge.next = self.Merge(pHead1.next,pHead2)
        else:
            pMerge = pHead2
            pMerge.next = self.Merge(pHead1,pHead2.next)
        return pMerge

        """
        脑残的想法？归并排序的想法
        """
        # if pHead1 ==None and pHead2:
        #     return pHead2
        # if pHead2 == None and pHead1:
        #     return pHead1
        # if pHead1==None and pHead2==None:
        #     return None
        # pMerge = ListNode(0)
        # while pHead1 and pHead2:
        #     if pHead1.val <pHead2.val:
        #         pMerge.next=pHead1
        #         pHead1=pHead1.next
        #         pMerge=pMerge.next
        #     elif pHead1.val >pHead2.val:
        #         pMerge.next=pHead2
        #         pHead2=pHead2.next
        #         pMerge=pMerge.next
        #     else:
        #         pMerge.next=pHead1
        #         pMerge=pMerge.next
        #         pMerge.next=pHead2
        #         pMerge=pMerge.next
        #         pHead1=pHead1.next
        #         pHead2=pHead2.next
        #
        # if pHead1:
        #     pMerge.next = pHead1
        # if pHead2:
        #     pMerge.next = pHead2