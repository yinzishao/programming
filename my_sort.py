#coding=utf-8
__author__ = 'yinzishao'

class Sort():
    """
                插入排序
    """
    #直接插入排序
    def straight_insertion_sort(self,array):
        for i in range(1,len(array)):
            l = i -1
            while l>=0 and array[l+1]<array[l]:
                array[l+1],array[l] = array[l],array[l+1]
                l-=1
        return array
    #折半插入排序
    def binary_insertion_sort(self,array):
        for i in range(1,len(array)):
            temp =array[i]
            start =0
            end = i-1
            while start <=end:
                mid = (start+end)/2
                if(array[mid]==temp):
                    start = mid
                    break
                if(array[mid]<temp):
                    start = mid+1
                else:
                    end = mid-1
            for l in range(start,i)[::-1]:
                array[l+1],array[l]=array[l],array[l+1]
        return array
    #希尔排序(增量的选择没有实现)
    def shell_sort(self,array,dk=[5,3,1]):
        print "============shell's sort==============="
        for i in dk:
            for l in range(i,len(array)):
                m = l
                while m-i >=0 and array[m]<array[m-i]:
                    array[m-i],array[m]=array[m],array[m-i]
                    m=m-i


        return array
    """
                #交换排序
    """
    #冒泡排序
    def bubble_sort(self,array):
        # for i in range(len(array))[::-1]:
        for i in range(1,len(array))[::-1]:
            l = 0
            flag =True
            #一定要遍历一遍所有的才能知道下次还要不要冒泡,所以不能用while
            for l in range(0,i):
                if array[l+1]<array[l]:
                    array[l+1],array[l]=array[l],array[l+1]
                    flag=False
            if flag:
                break
        return array
    #快速排序
    def quick_sort(self,array):
        return self.q_sort(array,0,len(array)-1)
    def q_sort(self,array,start,end):
        if start<end:
            p = self.Partition(array,start,end)
            self.q_sort(array,start,p-1)
            self.q_sort(array,p+1,end)
        return array
    def Partition(self,array,start,end):
        temp = array[start]
        s = start
        e = end
        #注意两点，一是一开始的时候不要比较start。所以要<=
        #二是要从后面开始
        while s<e:
            while array[e]>=temp and s < e:
                e-=1
            while array[s]<=temp and s < e:
                s+=1

            array[s],array[e]=array[e],array[s]

        array[s],array[start]=array[start],array[s]
        return s
    """
    选择排序
    """
    #简单选择排序
    def simple_selectiion_sort(self,array):
        for i in range(len(array))[::-1]:
            max_temp_index = 0
            for l in range(i):
                if array[l+1]>array[max_temp_index]:
                    max_temp_index=l+1
            # if(max_temp_index!=0)
            array[i],array[max_temp_index]=array[max_temp_index],array[i]
        return array
    #堆排序
    def heap_sort(self,array):
        #建初堆
        for i in range(1,len(array)/2+1)[::-1]:
            self.heap_adjust(array,i,len(array))

        for l in range(len(array))[::-1]:
            array[0],array[l]=array[l],array[0]
            self.heap_adjust(array,1,l)
        return array


    #调整堆，注意i是树的下标从1开始，与数组差1
    #注意增加结束下标变量，因为交换后结束下标提前一位了
    def heap_adjust(self,array,i,m):
        while 2*i<=m:
            if(2*i+1<=m and array[2*i]>array[2*i-1]):
                max = 2*i
            else:
                max = 2*i-1
            if array[i-1]>=array[max]:
                break
            else:
                array[i-1],array[max]=array[max],array[i-1]
                # error : i=max  max是数组的时候的下标，加上1才是树的下标
                i=max+1
    """
    归并排序
    """
    #归并排序

    def merging_sort(self,array):
        return self.m_sort(array,0,len(array)-1)
    def m_sort(self,array,start,end):
        if start<end:
            mid =(start+end)/2
            larray = self.m_sort(array,start,mid)
            rarray = self.m_sort(array,mid+1,end)
            self.merge(array,larray,rarray,start,end)
        return array[start:end+1]
    def merge(self,array,larray,rarray,start,end):
        li=0
        ri=0
        while li <len(larray) and ri <len(rarray):
            if larray[li] <rarray[ri]:
                array[start]=larray[li]
                li+=1
            else:
                array[start]=rarray[ri]
                ri+=1
            start+=1
        while li<len(larray):
            array[start]=larray[li]
            start+=1
            li+=1
        while ri<len(rarray):
            array[start]=rarray[ri]
            start+=1
            ri+=1

print Sort().straight_insertion_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().binary_insertion_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().shell_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().bubble_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().bubble_sort([5,4,3,2,1])
print Sort().quick_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().simple_selectiion_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().heap_sort([49,38,65,97,76,13,27,49,55,04])
print Sort().merging_sort([49,38,65,97,76,13,27,49,55,04])

tetest=[1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663]
print Sort().merging_sort(tetest)[23]
# print Sort().merging_sort([49,38])




