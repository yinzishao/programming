# -*- coding:utf-8 -*-
class Solution:
    def reOrderArrayIII(self, array):
        # write code here
        if array==[]:
            return []
        for i in range(len(array)):
            if array[i]%2==1:
                temp = i
                for j in range(0,i)[::-1]:
                    if array[j]%2==0:
                        array[temp],array[j]=array[j],array[temp]
                        temp=j
        return array
    #上一种方法的优化。记录第一个偶数的下标，每次移到都是下标加一。省去很多的步骤
    def reOrderArray(self, array):
        # write code here
        if array==[]:
            return []
        oufirst=0
        while oufirst<len(array):
            if array[oufirst]%2==0:   #找出第一个偶数
                break

            oufirst+=1
        for i in range(len(array)):

            if array[i]%2==1:
                temp = i
                for j in range(oufirst,i)[::-1]:

                    array[temp],array[j]=array[j],array[temp]
                    temp=j
                oufirst+=1
        return array


    def reOrderArrayII(self,array):
        if array==[]:
            return []
        """
        while 循环遍历比for循环要慢！！！！
        """
        # i=0
        # while i<len(array):
        #     if array[i]%2==0:   #找出第一个偶数
        #         j=i+1
        #         break
        #
        #     i+=1
        #
        # while j < len(array):
        #     if array[j]%2==1:#找出后面的第一个奇数
        #         for k in range(i,j)[::-1]:
        #             array[k+1],array[k]=array[k],array[k+1]
        #         i+=1
        #
        #     j+=1
        #

        oufirst=0
        while oufirst<len(array):
            if array[oufirst]%2==0:   #找出第一个偶数
                j=oufirst+1
                break

            oufirst+=1
        for i in range(j,len(array)):

            if array[i]%2==1:
                temp = i
                for j in range(oufirst,i)[::-1]:

                    array[temp],array[j]=array[j],array[temp]
                    temp=j
                oufirst+=1
        return array

# print Solution().reOrderArrayII(range(10))

#
import time
start= time.time()
Solution().reOrderArrayII(range(10000))
end = time.time()
print (end-start)
start= time.time()
Solution().reOrderArray(range(10000))
end = time.time()
print (end-start)




            