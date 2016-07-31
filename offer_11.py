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
思路：
如果我们在遍历时维持两个指针，第一个指针从链表的头指针开始遍历，在第k-1步之前，第二个指针保持不动；
在第k-1步开始，第二个指针也开始从链表的头指针开始遍历。
由于两个指针的距离保持在k-1，当第一个（走在前面的）指针到达链表的尾结点时，第二个指针（走在后面的）指针正好是倒数第k个结点。
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