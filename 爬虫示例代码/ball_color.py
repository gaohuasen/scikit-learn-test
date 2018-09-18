# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:26:54 2018

@author: Admin
"""
count = 0
def perm(n,begin,end):
    '''
    递归的方法把这10个球所有的颜色可能性打印出来
    '''
    global count
    if begin == end:  #基准点
        print(n)
        count += 1
    else:
        perm(n,begin+1,end)
        n[begin] = (n[begin]+1)%2
        perm(n,begin+1,end)
        
L = [0,0,0,0,0,0,0,0,0,0]
perm(L,0,len(L))
print(count)