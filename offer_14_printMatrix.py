# -*- coding:utf-8 -*-
"""

题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

遇到一个问题就是测试的时候result总是追加在上次result的后面。
发现是因为测试是用同一个solution类的，所以每次调用printMatrix时都需要清空result。最好是在方法里面初始化
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    # result=[]
    def printMatrix(self, matrix):
        # write code here
        if matrix == None:
            return None
        if not isinstance(matrix[0],list):
            return matrix
        else:
            flag = matrix
            self.result = []
            self.start(0,0,flag)
            return self.result

    def start(self,w,l,flag):
        width = len(flag)
        length = len(flag[0])
        self.result.append(flag[w][l])
        flag[w][l]=False
        if  l+1<length and flag[w][l+1] !=False :
            if w>0 and flag[w-1][l] !=False:
                self.start(w-1,l,flag)
            else:
                self.start(w,l+1,flag)
        elif w+1<width and flag[w+1][l]!=False:
            self.start(w+1,l,flag)
        elif l-1>=0 and flag[w][l-1] != False:
            self.start(w,l-1,flag)
        elif w-1>=0 and flag[w-1][l] != False:
            self.start(w-1,l,flag)


# print Solution().printMatrix([[-1,2,3,4],[10,11,-1,5],[9,8,7,6]])
print Solution().printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])