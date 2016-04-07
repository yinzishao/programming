# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre ==[]:
            return None
        treenode = TreeNode(pre[0])
        if len(pre)==1 and len(tin)==1:
            return treenode
        left_length = tin.index(pre[0])
        treenode.left = self.reConstructBinaryTree(pre[1:left_length+1],tin[0:left_length])
        treenode.right = self.reConstructBinaryTree(pre[left_length+1:],tin[left_length+1:])
        return treenode

    def reConstructBinaryTree_1(self, pre, tin):
        # write code here
        if pre ==[]:
            return None

        root = pre.pop(0)

        indexOfRootInTin = tin.index(root)

        tree = TreeNode(root)

        tree.left = self.reConstructBinaryTree_1(pre[:indexOfRootInTin],tin[:indexOfRootInTin])

        tree.right = self.reConstructBinaryTree_1(pre[indexOfRootInTin:],tin[indexOfRootInTin+1:])

        return tree

def print_tree(treenode):
    import Queue
    que = Queue.Queue()
    if treenode:
        que.put(treenode)
        # print
    while not que.empty():
        treenode_que = que.get()
        print treenode_que.val

        if treenode_que.left!=None:
            que.put(treenode_que.left)
        if treenode_que.right!=None:
            que.put(treenode_que.right)



if __name__ =="__main__":
    a = Solution().reConstructBinaryTree_1([1,2,3,4,5,6,7],[3,2,4,1,6,5,7])

    print_tree(a)
    # a = [1,2,3]
    # print a[1:]

