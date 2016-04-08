# -*- coding:utf-8 -*-
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