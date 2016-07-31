# -*- coding:utf-8 -*-
__author__ = 'yinzishao'
"""
题目描述

有一个长为n的数组A，求满足0≤a≤b<n的A[b]-A[a]的最大值。

给定数组A及它的大小n，请返回最大差值。(贪心)
测试样例：
"""
class LongestDistance:
    def getDis(self, A, n):
        # write code here
        max = 0
        for i in range(0,n-1):
            for m in range(i,n-1):
                temp_max = A[m+1] - A[i]
                if(temp_max > 0 and temp_max > max):
                    max= temp_max
        return max


    #     正确答案o(n)：循环一次与最小的比较选出最大差值
    def getDis2(self,A,n):
        dis = 0
        min = A[0]
        for i in range(1,n):
            if(A[i]-min > dis):
                dis = A[i]-min
            if(A[i]<min):
                min = A[i]
        return dis


if __name__ == "__main__":
    a = LongestDistance().getDis2([2,7,1,2],4)
    print a