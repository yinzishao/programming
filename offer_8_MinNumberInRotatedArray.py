# -*- coding:utf-8 -*-
"""
旋转数组的最小数字
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减序列的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        return self.minBinarySearch(rotateArray)

    def minBinarySearch(self,rotateArray):  #special situation
        if rotateArray ==[]:
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        midlen=len(rotateArray)/2
        mid = rotateArray[midlen]
        if(mid<rotateArray[midlen-1]):
            return mid
        if mid == rotateArray[0] and mid ==rotateArray[-1]:
            return self.search(rotateArray)
        if mid < rotateArray[0]:
            return self.minBinarySearch(rotateArray[:midlen+1])
        elif mid >rotateArray[-1]:
            return self.minBinarySearch(rotateArray[midlen:])
        else:
            return rotateArray[0]
    def search(self,rotateArray):
        for i in rotateArray:
            if i!=rotateArray[0]:
                return i

print Solution().minNumberInRotateArray([1,2,2,2,2,2])