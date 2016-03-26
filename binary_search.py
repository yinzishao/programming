#coding=utf-8
__author__ = 'yinzishao'

# 题目描述
#
# 对于一个有序数组，我们通常采用二分查找的方式来定位某一元素，请编写二分查找的算法，在数组中查找指定元素。
#
# 给定一个整数数组A及它的大小n，同时给定要查找的元素val，请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。若该元素出现多次，请返回第一次出现的位置。
# 测试样例：
#
# [1,3,5,7,9],5,3
#
# 返回：1
#


class BinarySearch:
    def getPos(self, A, n, val):
        # write code here
        mid = n/2
        if val == A[mid]:
            return mid
        elif(val < A[mid]):
            return self.searchVal(A,0,mid-1,val)
        else:
            return self.searchVal(A,mid+1,n-1,val)


    def searchVal(self,A,index,end,val):
        if end >=index:
            mid = (index+end)/2
            if val == A[mid]:
                return mid
            elif val < A[mid]:
                return BinarySearch().searchVal(A,index,mid-1,val)
            else:
                return BinarySearch().searchVal(A,mid+1,end,val)
        return -1

    """
    # 参考答案
    def getPos(self,A,n,val):
        if(n<=0 || A==None) return -1;
        l=0
        r=n-1
        mid = (l+r)/2
        while(l<=r):
            if(A[mid]=val):
                r=mid
            elif(A[mid]>val):
                r=mid-1
            else:
                l=mid+1
        if A[l]==val:       #如果一开始就找到mid，虽然还会继续找最左边的第一次出现的位置，但最后都l与r会重叠在一起。
            return l
        else:
            return -1


    """

if __name__ == "__main__":
    print BinarySearch().getPos([1,3,5,7,9],5,3)