# -*- coding:utf-8 -*-
"""

题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

解题思路：
当长度小于等于2的时候无论怎么排都可以成立
当长度大于2的时候：
    先获取最后一个元素
    从list前一直找出比最后一个元素大的元素下标。以此为分隔。
    当后端没有比最后一个元素还小的元素的时候。说明以最后一个元素为结点的二叉搜索树没有问题。
    把前后两端以此递归。
"""
class Solution:
    flag = True
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        last = sequence[-1]
        i = 0
        while i < len(sequence)-1 and sequence[i]<last  :
            i+=1
        j = i
        while j<len(sequence)-1:
            if sequence[j]<last:
                self.flag = False

            j+=1
        front_seq = sequence[:i]
        pre_seq = sequence[i:-1]

        if len(front_seq)>2:
            self.VerifySquenceOfBST(front_seq)
        if len(pre_seq)>2:
            self.VerifySquenceOfBST(pre_seq)
        return self.flag

    def judge(self,list):
        if len(list) <=2:
            return True
        i = len(list)-1
        while(i>0 and list[i-1] > list[-1]):
            i-=1
        for k in range(0,i):
            if list[k]>list[-1]:
                return False
        return self.judge(list[:i]) and self.judge(list[i:-1])


# print Solution().VerifySquenceOfBST([1,2,4,3,6,1,7,5])
print Solution().judge([1,2,4,3,6,8,7,5])
# print [1,2][1:-1]
"""C++
class Solution {
    bool judge(vector<int>& a, int l, int r){
        if(l >= r) return true;
        int i = r;
        while(i > l && a[i - 1] > a[r]) --i;
        for(int j = i - 1; j >= l; --j) if(a[j] > a[r]) return false;
        return judge(a, l, i - 1) && (judge(a, i, r - 1));
    }
public:
    bool VerifySquenceOfBST(vector<int> a) {
        if(!a.size()) return false;
        return judge(a, 0, a.size() - 1);
    }
};
"""