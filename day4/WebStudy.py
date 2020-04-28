# coding=utf-8
from flask import Flask
from flask import request

def triangles():
    L = [1]
    while True:
        yield L
        L.insert(0,0)
        L.append(0)
        list1 = L[:(len(L) - 1)]
        for i in range(len(list1)-1):
            list1[i] = L[i] + L[i + 1]
        L = list1[:]
triangles().send()
        # 1
        # 1 1
        #
        # 0 1 1 0
        # 1 2 1

