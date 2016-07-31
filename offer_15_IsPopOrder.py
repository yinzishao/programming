# -*- coding:utf-8 -*-
"""

题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。

"""
# class Solution:
#     def IsPopOrder(self, pushV, popV):
#         # write code here
#
#         i=0
#         tempV=[]
#         self.IsPopOrder(pushV,popV,tempV)
#
#     def IsPopOrder(self, pushV, popV,tempV):
#         i=0
#         if  tempV == [] or popV[0] != tempV[0] :
#
#             while i < len(pushV):
#                 if pushV[i] != popV[0]:
#                     tempV.append(pushV[i])
#                     i+=1
#                 else:
#                     self.IsPopOrder(pushV[i+1:],popV[1:],tempV)
#         else:
#             tempV=tempV[0:-2]
#             self.IsPopOrder(pushV,popV[1:],tempV)


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] and popV == []:
            return False

        tempV =[]
        while popV !=[]:
            first_of_popV = popV[0]
            del popV[0]

            if tempV !=[]:
                if tempV[-1] == first_of_popV:
                    flag = True
                    del tempV[-1]
                    continue
            if pushV == [] and popV !=[] :
                flag = False
                break
            for i in pushV:
                if i != first_of_popV:
                    flag = False
                    tempV.append(i)
                    if i == pushV[-1]:  #修改
                        return False
                else:
                    flag = True
                    pushV = pushV[pushV.index(i)+1:]
                    break
        return flag

print Solution().IsPopOrder([1,2,3,4,5],[4,5,3,2,1])

"""C++
class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        if(pushV.size() == 0) return false;
        vector<int> stack;
        for(int i = 0,j = 0 ;i < pushV.size();){
            stack.push_back(pushV[i++]);
            while(j < popV.size() && stack.back() == popV[j]){
                stack.pop_back();
                j++;
            }
        }
        return stack.empty();
    }
};
"""