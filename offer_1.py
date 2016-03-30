# -*- coding:utf-8 -*-
__author__ = 'yinzishao'
"""
题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
输入描述:

array： 待查找的二维数组
target：查找的数字
"""

class Solution:
    # array 二维列表
    def Find(self, array, target):
        # array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
        # target=7
        chang_temp= len(array[0])-1
        kuan = kuan_temp=len(array)-1
        while(chang_temp>=0 and kuan_temp>=0):
            print kuan-kuan_temp,chang_temp
            temp = array[kuan-kuan_temp][chang_temp]
            if temp==target:
                return True
            elif target > temp:
                kuan_temp-=1
            else:
                chang_temp-=1
        return False



        # write code here

if __name__ =="__main__":

    print Solution().Find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],7)