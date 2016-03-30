#coding=utf-8
__author__ = 'yinzishao'
"""

题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串

    def replaceSpace(self, s):
        # write code here
        i=0
        for a in s:
            if a ==" ":
                i+=1


if __name__ =="__main__":
    print Solution().replaceSpace("yin zi shao")