# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:55:03 2018

@author: Admin
"""
import threading

def f():
    while True:
        pass
    
if __name__ == '__main__':
    t = threading.Thread(target=f)
    t.start()
    
    while True:
        pass