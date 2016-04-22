#coding=utf-8
"""
[编程题] 地域划分

现在有一块长条形的土地，这个土地我们可以看成是由n块小方格连接而成的(这些小方格我们可以将之编号为1到n)。而我们需要将其划分成两个部分，分别种上不同的作物(即作物A和B)，划分必须在某两个小方格之间进行，或者在土地的最左端或最右端，若划分在第i块到第i+1块间进行，则划分后，第1至第i块地种A，剩下的地种B。现在有一些专家对土地进行了检测，他们每个人评估了每块土地适合种的作物。请你找到一个合适的划分，使得其与所有专家的评估最吻合，也就是说，你划分到A而专家评估为B的次数和你划分到B而专家评估为A的次数之和最小。

输入描述:

每组数据给定一个专家评估表land(其中0为评估A，1为评估B)，以及小块数量n(1≤n≤300)，专家评估次数m(1≤m≤300)



输出描述:

请返回你的划分,即i和i+1。若在最左端，则输出0，1；在最右端则输出n,n+1。若有多解输出最靠左的划分。


输入例子:

[[1,1,1,1],[0,0,0,0],[1,0,1,1]],4,3


输出例子:

[0,1]

我的思路：
先把所有专家的评测集合，变成一个数组[[1,1,1,1],[0,0,0,0],[1,0,1,1]]变成[1,-1,1,1]
-1 表示预测A的次数 为1次，+1为预测B的次数为1
然后从左到右算出每个划分情况的A错误次数(注意4块地有5种情况，最左边A错误为0)
然后从右到左算出每个划分情况的B错误次数（最右边B错误为0）
加起来最小的就是答案

"""
__author__ = 'yinzishao'

class Partition:
    # land 二维list，每个项为专家给出的划分，例如[[1,1,1,1],[0,0,0,0],[1,0,1,1]]
    # 请函数返回一个划分的list，例如 [0,1]
    def getPartition(self, land, n, m):
        # write code here
        # return [0, 1]
        res = [0 for i in range(n)]
        # print res
        for i in land:
            for index,value in enumerate(i):
                if value ==1:
                    res[index]+=1
                else:
                    res[index]-=1
        # return res
        # print res
        a_cuo=[0 for i in range(len(res)+1)]
        b_cuo=[0 for i in range(len(res)+1)]
        a_cuo_num=0
        b_cuo_num=0
        for i,v in enumerate(res):
            if v>0:
                a_cuo_num+=v
            a_cuo[i+1]=a_cuo_num
        for i,v in enumerate(res[::-1]):
            if v<0:
                b_cuo_num-=v
            b_cuo[i+1]=b_cuo_num
        b_cuo.reverse()
        min_error=a_cuo[0]+b_cuo[0]
        min_error_index=0
        for i in range(len(res)+1):
            if a_cuo[i]+b_cuo[i]<min_error:
                min_error=a_cuo[i]+b_cuo[i]
                min_error_index=i

        return [min_error_index,min_error_index+1]
print Partition().getPartition([[1,1,1,1],[0,0,0,0],[1,0,1,1]],4,3)