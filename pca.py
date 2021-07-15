import numpy as np
import sys
from numpy import linalg as LA
import matplotlib.pyplot as plt
li = []

filename = sys.argv[-1]
file = open(str(filename), 'r')
for each in file:
    li1 = each.strip("\n")
    li1 = li1.split(",")
    li1 = [float(x) for x in li1]
    li.append(li1)

arr = np.array(li)

N,D = len(arr),len(arr[0])
avg = []
for a in range(D):
	avg.append(np.mean(arr[:][a]))
#print(avg)
std = []
for a in range(D):
	std.append(np.std(arr[:][a]))
#print(std)

for a in range(D):
	arr[:][a] = (arr[:][a]-avg[a])/std[a]
print("After transformation of mean and std\n",arr[:5])
print("-"*100)
actual_data = arr
arr = arr.T
arr = np.cov(arr)
print("After finding cov\n",arr)
print("-"*100)
w, v = LA.eig(arr)
idx = w.argsort()[::-1]   
w = w[idx]
v = v[:,idx]
print("Eigenvalue\n",w)
print("Eigenvector\n",v)
print("-"*100)
v = v[:][:2].T
print(v)
transformed_data = np.matmul(actual_data,v)
print("Transformed data\n",transformed_data[:5])
plt.figure(figsize=(10,6))
plt.axis([-15, 15, -15, 15])
x = transformed_data[:,0]
y = transformed_data[:,1]
plt.scatter(x, y)
plt.show()


