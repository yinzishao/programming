# -*- coding:utf-8 -*-
"""

题目描述
输入一个链表，反转链表后，输出链表的所有元素。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
__author__ = 'yinzishao'
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None :
            return None
        pNode = pHead
        pPre = None

        while pNode.next!=None:
            pNext = pNode.next

            pNode.next=pPre
            pPre=pNode
            pNode=pNext
        pNode.next=pPre
        return pNode