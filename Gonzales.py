#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:23:58 2019

@author: kbg
"""
import numpy as np
from math import sqrt

def Gonzales(data, c1, k=3):
    n = len(data)
    assignments = dict([(_, 0) for _ in range(n)])
    clusters = np.empty((k, len(c1)))
    clusters[0,:] = c1
    for i in range(1,k):
        m = 0
        clusters[i,:] = data[0]
        for j in range(n):
            if dist(data[j,:], clusters[assignments[j], :]) > m:
                m = dist(data[j,:], clusters[assignments[j], :])
                clusters[i,:] = data[j,:]
                
        for j in range(n):
            if dist(data[j,:], clusters[assignments[j], :]) > dist(data[j,:], clusters[i,:]):
                assignments[j] = i
    arr = [dist(d, clusters[assignments[idx],:]) for idx,d in enumerate(data)]
    max3cenCost = max(arr)
    mean3Cost = sqrt(sum([x**2 for x in arr])/len(arr))
    
    data = np.append(data, np.array([[i] for i in list(assignments.values())]), axis=1)
    return data, max3cenCost, mean3Cost, clusters


def dist(a,b):
    return np.linalg.norm(a-b)