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
plt.xlim([0, 10000000])
plt.ylim([0, 10000000])
plt.scatter(dataset.price,dataset.odometer, s =10, c = "c", marker = "o", alpha = 0.5)
plt.show()
x_array =  np.array(dataset)

# print(x_array[0][1])

# print(c[0])

# arr = []
# arr.append([])
# i=0
# k=0
# while(i<10):
#     while(k<10):
#         arr[i].append('1')
#         k=k+1
#     i=i+1

# arr[0].append('aa1')
# arr[0].append('aa2')
# arr.append([])
# arr[1].append('aa1')
# arr[1].append('aa2')


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
            
            proc_hasil[k].append(round(hasil,2))
            s=s+1
        k=k+1
    return proc_hasil




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



def means(minC,proc_arr):
    i=0
    x=0
    mean_arr=[]
    while(i<100):
        k=0
        totx=0
        toty=0
        count=0
        mean_arr.append([])
        while(k<len(proc_arr)):
            if(minC[k]==i):
                totx=totx+proc_arr[k][1]
                toty=toty+proc_arr[k][2]
                count=count+1
            k=k+1
        if(count==0):
            count=1
        else:
            x=x+1
        mean_arr[i].append(round(totx/count,2))
        mean_arr[i].append(round(toty/count,2))
        i=i+1
    print("tyhiss",x)
    return mean_arr


def process1(proc_arr,mean_arr):
    proc_hasil=[]
    # for k in range(0,len(proc_arr)):
    #     for s in range(0,len(c)):
    k=0
    
    while(k<=len(proc_arr)-1):
        # print(k)
        proc_hasil.append([k])
        s=0
        while(s<=len(mean_arr)-1):
            pre=abs(((proc_arr[k][1]**2)-(mean_arr[s][0]**2))+((proc_arr[k][2]**2)-(mean_arr[s][1]**2)))
            hasil = math.sqrt(pre)
            proc_hasil[k].append(round(hasil,2))
            s=s+1
        k=k+1
    return proc_hasil



proc_arr=x_array
c=np.random.randint(1, len(x_array),100)
proc_hasil=process(proc_arr,c)
minC=[]
minC=minClus(proc_hasil)
minC_it=[]
# mean_arr=means(minC,proc_arr)
# proc_hasil=process1(proc_arr,mean_arr)
# print(proc_hasil)
a=True
i=0
while(a==True):
    mean_arr=means(minC,proc_arr)
    proc_hasil=process1(proc_arr,mean_arr)
    minC_it=minClus(proc_hasil)
    if(minC_it!=minC):
        a=True
        minC=minC_it
        i=i+1
        print(i)
    else:
        a=False

# print(minC_it)

# MAKING ARRAY PLOT (clust,array[index proc_arr])
# plot_arr=[]
# i=0
# while(i<len(minC_it)):
#     k=0
#     plot_arr.append([])
#     while(k<len(proc_arr)):
#         if(minC==i):
#             plot_arr[i].append(k)
#         k=k+1
#     i=i+1

# print(plot_arr)
plt.plot()

plt.title('k means centroids')
mean_arr=np.array(mean_arr)
for i in range(0,len(proc_arr)):
    print(i)
    plt.scatter(proc_arr[i][1], proc_arr[i][2], color="b", marker="o")
plt.xlim([0, 10000000])
plt.ylim([0, 10000000])

plt.scatter(mean_arr[:,[0]], mean_arr[:,[1]], marker="x", color='r')
plt.show()



