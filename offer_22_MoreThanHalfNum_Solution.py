# -*- coding:utf-8 -*-
"""

题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""
# -*- coding:utf-8 -*-
class Solution:
    result =0
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers in [None,[]]:
            return 0
        if len(numbers) ==1:
            return numbers[0]
        return self.search(numbers,0,len(numbers)-1)


    def search(self,number,start,end):
        p = self.Pation(number,start,end)
        mid =len(number)/2+1
        while p != mid:

            if p>mid:
                p = self.Pation(number,start,p-1)
            else:
                p = self.Pation(number,p+1,end)
        result = number[mid]
        if self.CheckMoreThanHalf(number,result):
            result=0
        return result
    def CheckMoreThanHalf(self,number,result):
        if number.count(result)*2<len(number):
            return True
        return False

    def Pation(self,list,start,end):
        s = start
        temp = list[start]
        while start<end:
            while list[end]>=temp and start<end:
                end-=1

            while list[start]<=temp and start<end:
                start+=1

            list[start],list[end]= list[end],list[start]
        list[s]=list[start]
        list[start]=temp
        return start

print Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])