# -*- coding:utf-8 -*-
__author__ = 'yinzishao'
"""
一开始n=0，输出也是0.
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        fib=lambda n:0 if n==0 else 1 if 0<n<=2 else fib(n-1)+fib(n-2)
        return fib(n)

    def fiba(self,n):
        return  int(n==0 and "0" or ( 0<n<=2 and 1 ) or self.fiba(n-1)+self.fiba(n-2))

    def fibb(self,n):
        x,a,b=0,0,1
        while x<n:
            a,b=b,a+b
            x+=1
        return a


if __name__ == "__main__":
    print  Solution().fibb(3)