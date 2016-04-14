# -*- coding:utf-8 -*-
"""

题目描述
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    result = []
    def FindPath(self, root, expectNumber):
        # write code here
        if root ==None:
            return []

        self.result = []
        self.Find(root,expectNumber,root.val,[root.val])
        return self.result
    def Find(self,cur_root,expectNumber,cur_sum,cur_list):

        if cur_root.left ==None and cur_root.right == None and cur_sum == expectNumber:
            a= cur_list[:]
            self.result.append(a)
        if cur_root.left !=None:
            if cur_sum + cur_root.left.val <=expectNumber:
                cur_list.append(cur_root.left.val)
                self.Find(cur_root.left,expectNumber,cur_sum + cur_root.left.val,cur_list)
                cur_list.pop()
        if cur_root.right !=None:
            if cur_sum + cur_root.right.val <=expectNumber:
                cur_list.append(cur_root.right.val)
                self.Find(cur_root.right,expectNumber,cur_sum + cur_root.right.val,cur_list)
                cur_list.pop()
# 测试用例
root = TreeNode(10)
left  = TreeNode(5)
right  = TreeNode(12)
sub_left  = TreeNode(4)
sub_right  = TreeNode(7)
root.left = left
root.right = right
left.left =sub_left
left.right =sub_right

print Solution().FindPath(root,15)

"""c++
class Solution {
    vector<vector<int> >allRes;
    vector<int> tmp;
    void dfsFind(TreeNode * node , int left){
        tmp.push_back(node->val);
        if(left-node->val == 0 && !node->left && !node->right)
            allRes.push_back(tmp);
        else {
            if(node->left) dfsFind(node->left, left-node->val);
            if(node->right) dfsFind(node->right, left-node->val);
        }
        tmp.pop_back();
    }
public:
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
        if(root) dfsFind(root, expectNumber);
        return allRes;
    }
};
"""



# list = [1]
# list.append(2)
# list.insert(2,3)
# print list.pop()
# l = ['a', 'b', 'c', [1, 2, 3]]
# import copy
# a = copy.copy(l)
# b = copy.deepcopy(l)
# a.append('e')
# b.append('f')
# print a, b, l
# a[3][2] = 'x'
# b[3][2] = 'y'
# print a, b, l
