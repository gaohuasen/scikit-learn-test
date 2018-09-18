# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:05:17 2018

@author: Admin
"""

import hashlib

def hashStr(strInfo):
    '''
    对字符串进行hash
    '''
    hashObj = hashlib.sha256()
    hashObj.update(strInfo.encode('utf-8'))
    return hashObj.hexdigest()

def hashFile(fileName):
    '''
    对文件进行hash
    '''
    hashObj = hashlib.sha256()
    with open(fileName,'rb') as f:
        while True:
            chunk = f.read(2048)
            if not chunk:
                break
            hashObj.update(chunk)
    return hashObj.hexdigest()

#print(hashStr('hello'))
print(hashFile())