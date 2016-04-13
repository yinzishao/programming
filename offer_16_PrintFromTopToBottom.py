# -*- coding:utf-8 -*-
"""
广度优先遍历
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        list = []
        if root==None:
            return []

        import Queue
        q = Queue.Queue()
        q.put(root)

        while not q.empty():
            current_root=q.get()
            list.append(current_root.val)
            if current_root.left != None:
                q.put(current_root.left)
            if current_root.right != None:
                q.put(current_root.right)
        return list


root = TreeNode(1)
left  = TreeNode(2)
right  = TreeNode(3)
root.left = left
root.right = right
print Solution().PrintFromTopToBottom(None)
# a = [2,1,2,2,3]
# del a[3]
# print a
# print a.pop(1),a
"""C++
class Solution {
public:
    vector<int> PrintFromTopToBottom(TreeNode *rt) {
        queue<TreeNode*> q;
        q.push(rt);
        vector<int> r;
        while(!q.empty()){
            rt = q.front(); q.pop();
            if(!rt) continue;
            r.push_back(rt -> val);
            q.push(rt -> left);
            q.push(rt -> right);
        }
        return r;
    }
};
"""