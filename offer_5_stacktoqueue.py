__author__ = 'yinzishao'
# -*- coding:utf-8 -*-
"""

题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""
class Solution:
    stack_a,stack_b= [],[]
    def push(self, node):
        # write code here
        # self.l.append(node)
        self.stack_a.append(node)

    def pop(self):
        if self.stack_b ==[]:
           # self.stack_b.extend(self.stack_a[::-1])
           self.stack_a.reverse()
           self.stack_b.extend(self.stack_a)
        # a= self.stack_b[len(self.stack_b)-1]
        # self.stack_b.pop(len(self.stack_b)-1)
        a = self.stack_b.pop()
        return a
        # return xx
        # a = self.l[0]
        # self.l.pop(0)
        # return a


s = Solution()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print s.pop()
print s.pop()
print s.pop()

"""C++代码
class Solution
{
public:
    void push(int node) {
        stack1.push(node);

    }

    int pop() {
        if (stack2.empty()){
            while(!stack1.empty()){
        		stack2.push(stack1.top());
                stack1.pop();
            }
        }
       	int a =stack2.top();
        stack2.pop();
        return a;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
"""