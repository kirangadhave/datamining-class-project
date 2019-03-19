import numpy as np
from math import sqrt

def dist(a,b):
    return np.linalg.norm(a-b)

def KPP(data, c1, k=3):
    n = len(data)
    
    assignments = dict([(_, 0) for _ in range(n)])
    clusters = np.empty([k,len(c1)])
    clusters[0, :] = c1
    
    for i in range(1,k):
        weights = np.array([dist(d, clusters[assignments[idx], :])**2 for idx,d in enumerate(data)])
        weights = weights/sum(weights)
        centerIdx = np.random.choice(list(range(n)), p=weights)
        clusters[i,:] = data[centerIdx,:]
        for j in range(n):
            if dist(data[j,:], clusters[assignments[j], :]) > dist(data[j,:], clusters[i,:]):
                assignments[j] = i
    arr = [dist(d, clusters[assignments[idx],:]) for idx,d in enumerate(data)]
    max3cenCost = max(arr)
    mean3Cost = sqrt(sum([x**2 for x in arr])/len(arr))
   
    data = np.append(data, np.array([[i] for i in list(assignments.values())]), axis=1)
