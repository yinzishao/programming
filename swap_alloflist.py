#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yinzishao'

"""
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,4,7]]
每个子list选一个的所有可能
"""

class Solution(object):
    def __init__(self):
        self.result = []
    def swap_alloflist(self,list):
        self.fenzi(list)
        return self.result
    def fenzi(self,list,res=[]):
        # if [] in (list,res):
        #     return False
        # else:
        #     return True
        if list ==[]:
            #因为res是引用的所以当res被pop的时候 result里面的res也被修改
            self.result.append(res[:])
        else:
            for i in list[0]:
                res.append(i)
                self.fenzi(list[1:],res)
                res.pop()


print Solution().swap_alloflist([[2,7,3],[4,5]])
# print [] in ([],[])
# print [1][1:]