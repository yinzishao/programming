# -*- coding:utf-8 -*-
"""
有一个整数数组，请你根据快速排序的思路，找出数组中第K大的数。

给定一个整数数组a,同时给定它的大小n和要找的K(K在1到n之间)，请返回第K大的数，保证答案存在。
测试样例：

[1,3,5,2,2],5,3

返回：2

注意第K大，而不是升序的第k-1个
"""
class Finder:
    # result = 0
    def findKth(self, a, n, K):
        # write code here
        if a ==None or K>n:
            return None
        return self.find(a,0,n-1,n-K)
        # return self.find(a,0,n-1,K-1)
        # return self.result
    def find(self,a,start,end,k):
        if start==end and start==k:
            # self.result = a[start]
            return a[start]
        if start<end:
            m = self.partion(a,start,end)
            if m ==k:
                # self.result=a[k]
                return a[m]
            if m <k:
                return self.find(a,m+1,end,k)
            if m>k:
                return self.find(a,start,m-1,k)
    def partion(self,a,start,end):
        s =start
        tmp = a[start]
        while start<end:
            while a[end]>=tmp and start<end:
                end-=1
            while a[start]<=tmp and start<end:
                start+=1
            a[start],a[end]=a[end],a[start]
        a[s],a[start]=a[start],a[s]
        return start

            
print Finder().findKth([1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663],49,24)