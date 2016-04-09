# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a,b,n=1,2,1
        while number>n:
            a,b,n=b,a+b,n+1

        return a
    def jumpFloor2(self,number):
        jf = lambda number : 1 if number ==1 else 2 if number==2 else jf(number-1)+jf(number-2)
        return jf(number)
print Solution().jumpFloor2(4)