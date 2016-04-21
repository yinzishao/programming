#coding=utf-8
"""
对于一个给定的字符串，我们需要在线性(也就是O(n))的时间里对它做一些变形。
首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把着个字符串中由空格隔开的单词反序，
同时反转每个字符的大小写。比如"Hello World"变形后就变成了"wORLD hELLO"。
输入描述:
给定一个字符串s以及它的长度n(1≤n≤500)
输出描述:
请返回变形后的字符串。题目保证给定的字符串均由大小写字母和空格构成。
输入例子:
"This is a sample",16
输出例子:
"SAMPLE A IS tHIS"

注意:当到达最后的时候，虽然没有空格还是要反转
    一开始虽然有空格但是不反转，所以需要设好反转判断的标准：end-start>1
"""
__author__ = 'yinzishao'

class Solution():
    def trans(self,str,l):
        if str == None:
            return None
        str_list=[i for i in str]
        start,end=0,0
        while end <l:
            if str_list[end].islower():
                str_list[end]=str_list[end].upper()
            elif str_list[end].isupper():
                str_list[end]=str_list[end].lower()
            # 注意当到达最后的时候，虽然没有空格还是要反转
            if end+1==l and end-start>0:
                self.swap(str_list,start,end)
                break
            if str_list[end]==" " :
                if end-start<2:
                    start=end+1
                else:
                    self.swap(str_list,start,end-1)
                    start=end+1
            end+=1
        self.swap(str_list,0,l-1)
        return "".join(str_list)
    def swap(self,str_list,start,end):
        while start<end:
            str_list[start],str_list[end]=str_list[end],str_list[start]
            start+=1
            end-=1
# print Solution().trans("This is a sample",16)
print Solution().trans("h ie",4)
