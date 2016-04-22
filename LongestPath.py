#coding=utf-8
"""
[编程题] 树上最长单色路径

对于一棵由黑白点组成的二叉树，我们需要找到其中最长的单色简单路径，其中简单路径的定义是从树上的某点开始沿树边走不重复的点到树上的另一点结束而形成的路径，
而路径的长度就是经过的点的数量(包括起点和终点)。而这里我们所说的单色路径自然就是只经过一种颜色的点的路径。你需要找到这棵树上最长的单色路径。
给定一棵二叉树的根节点(树的点数小于等于300，请做到O(n)的复杂度)，请返回最长单色路径的长度。这里的节点颜色由点上的权值表示，权值为1的是黑点，为0的是白点。

思路：
后序遍历
子结点不同的时候
当前节点与子节点比较。最大值为相同颜色的子节点的值+1
但要注意情况当结点与两个子节点的值相同的时候，
有两种情况：
一、可能是当前结点与两个子结点连在一起是最大的。(已经无法向上延伸)
二、可能是当前节点与两个子结点中的某个节点组成最大长度还可以向上延伸
"""
__author__ = 'yinzishao'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class LongestPath:
    max_sum=1
    def findPath(self, root):
        # write code here
        if root ==None:
            return None
        self.houxu(root)
        return self.max_sum
        # return 0
    def houxu(self,root):
        cur_num=1
        left_cur_num,right_cur_num=None,None
        if not root.left and not root.right:
            return 1


        if root.left:
            left_num = self.houxu(root.left)
            if root.val == root.left.val:
                left_cur_num=left_num+1
                cur_num=left_cur_num


        if root.right:
            right_num = self.houxu(root.right)
            if root.val == root.right.val:
                right_cur_num=right_num+1
                cur_num=right_cur_num

        if left_cur_num and right_cur_num:
            #如果两个结点跟当前结点一样，需要选出较大的向上延伸
            cur_num =left_cur_num>right_cur_num and left_cur_num or right_cur_num
            temp=left_cur_num+right_cur_num-1
            #先把两个子结点跟当前节点练成的最终路径（已经无法向上延伸）保存在max_num
            if temp>self.max_sum:
                self.max_sum=temp
        #返回较大的继续下去

        if cur_num>self.max_sum:
            self.max_sum=cur_num
        return cur_num

#测试例子：[0,0,1,1,0,0,1,1,1,0,0,1]
a = TreeNode(1)

root = TreeNode(0)
left  = TreeNode(1)
right  = TreeNode(1)
sub_left  = TreeNode(1)
sub_right  = TreeNode(1)
root.left = left
root.right = right
left.left =sub_left
left.right =sub_right

print LongestPath().findPath(root)
# print 0 == False