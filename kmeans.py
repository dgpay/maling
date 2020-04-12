import string 
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math



dataset = pd.read_csv(
        'datset.csv',
        delimiter=';', 
        )

dt=dataset.to_numpy()
print(dataset.head)


# col2=arr[:,[1]]
# col3=arr[:,[2]]
# col4=arr[:,[3]]
# i=0
# while(i<len(arr[:,[0]])):

#     i=i+1


# test
# x = [[2,5], [1,4]]
# for i, element in enumerate(x):
#     print(element[1])
#     if element[1] == 2:
#         x[i] = [5,5]

# print(x)
# a=[1,2,3,4,5,6,7,7,8,8,98,56,43,676,232,54,32,54,76,98]
# b=[1,5,10,20,15,30,62,48,15,26,26,5,35,4,5,12,35,62,23,12]
# print(dataset.price)

# plt.scatter(dataset.odometer,dataset.price, s =10, c = "c", marker = "o", alpha = 0.5)
# plt.show()


x_array =  np.array(dataset)
print(x_array)
# print(x_array[0][1])
proc_arr=x_array
c=np.random.randint(1, len(x_array),100)
# print(c[0])

arr = []
arr.append([])
# i=0
# k=0
# while(i<10):
#     while(k<10):
#         arr[i].append('1')
#         k=k+1
#     i=i+1

arr[0].append('aa1')
arr[0].append('aa2')
arr.append([])
arr[1].append('aa1')
arr[1].append('aa2')
print(arr)
print(len(proc_arr))
def process(proc_arr,c):
    proc_hasil=[]
    # for k in range(0,len(proc_arr)):
    #     for s in range(0,len(c)):
    k=0
    
    while(k<=len(proc_arr)-1):
        # print(k)
        proc_hasil.append([])
        s=0
        while(s<=len(c)-1):
            pre=abs(((proc_arr[k][1]**2)-(proc_arr[c[s]][1]**2))+((proc_arr[k][2]**2)-(proc_arr[c[s]][2]**2)))
            hasil = math.sqrt(pre)
            
            proc_hasil[k].append(hasil)
            s=s+1
        k=k+1
    return proc_hasil

proc_hasil=process(proc_arr,c)
print(proc_hasil[100][5])

print(len(proc_hasil))
# def minClus(proc_hasil,minC):
#     i=0
#     while(i<len(proc_hasil)):
#         k=0
#         minn=min(proc_hasil[i])
#         while(k<len(proc_hasil[i])):
#             if(minn == proc_hasil[i][k]):
#                 minC.append(k)
#             else:
#                 k=k+1
#         print(i)
#         i=i+1
#     return minC
def minClus(proc_hasil):
    i=0
    while(i<len(proc_hasil)):
        minC.append(proc_hasil[i].index(min(proc_hasil[i])))
        i=i+1
    return minC
minC=[]
minC=minClus(proc_hasil)
print(len(minC))
print(minC)

def means(minC,proc_arr):
    
    return 0



