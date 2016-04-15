# -*- coding:utf-8 -*-
"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。 结果请按字母顺序输出。
输入描述:

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

注意问题 字符串可能有重复
"""
class Solution:
    result = []
    def Permutation(self, ss):
        # write code here
        self.result = []
        if ss ==None or ss ==[]:
            return []
        self.fenzi([i for i in ss],0)
        #需要排序,无法自己写
        self.result.sort()
        return self.result
        #去重和排序
        # self.result = list(set(self.result))
        # self.result.sort()
        # return self.result

    def fenzi(self,ss,i):
        if i ==len(ss):

            self.result.append("".join(ss))

        for l in range(i,len(ss)):
            #去重 相当于self.result = list(set(self.result))
            if i !=l and ss[i]==ss[l]:
                continue

            self.swap(i,l,ss)
            i+=1
            self.fenzi(ss,i)
            i-=1
            # print ss
            self.swap(i,l,ss)
    def swap(self,i,e,ss):
        ss[i],ss[e] = ss[e],ss[i]

res = Solution().Permutation("abc")
# res.sort()
print res
"""
lass Solution {
public:
    vector<string> Permutation(string str) {
        //可以用递归来做
        vector<string> array;
        if(str.size()==0)
            return array;
        Permutation(array, str, 0);
        sort(array.begin(), array.end());
        return array;
    }

    void Permutation(vector<string> &array, string str, int begin)//遍历第begin位的所有可能性
    {
        if(begin==str.size()-1)
            array.push_back(str);
        for(int i=begin; i<=str.size()-1;i++)
        {
            if(i!=begin && str[i]==str[begin])//有重复字符时，跳过
                continue;
            swap(str[i], str[begin]);//当i==begin时，也要遍历其后面的所有字符；
                                    //当i!=begin时，先交换，使第begin位取到不同的可能字符，再遍历后面的字符
            Permutation(array, str, begin+1);//遍历其后面的所有字符；

            swap(str[i], str[begin]);//为了防止重复的情况，还需要将begin处的元素重新换回来

            /*举例来说“abca”，为什么使用了两次swap函数
                交换时是a与b交换，遍历；
                交换时是a与c交换，遍历；（使用一次swap时，是b与c交换）
                交换时是a与a不交换；
                */
        }
    }
};
"""