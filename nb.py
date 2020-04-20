from collections import Counter
import csv
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
datset = pd.read_csv(
        'train.csv',
        delimiter=',',

        )


dataset=np.array(datset)
print(dataset[1])
p =['high','normal','low','very low']
c =['excellent','good','like new','fair']
o =['high','medium','low']
t =['automatic','manual','other']


def data(dataset,score):
    a=0
    r=0
    while(r<len(dataset)):
        if(dataset[r][4]==score):
            a=a+1
        r=r+1
    return a

JumBuy =data(dataset,1)
print(JumBuy)
JumNotBuy =data(dataset,-1)
print(JumNotBuy)
totColmBuy = len(dataset[4])
PY=JumBuy/totColmBuy
PN=JumNotBuy/totColmBuy
# arr = []
# arr.append([])
# i=0
# k=0
# while(i<10):
#     while(k<10):
#         arr[i].append('1')
#         k=k+1
#     i=i+1
# print(arr)
def frekuensi(kol,indikator,dataset,score):
    a=0
    for i in range (0,len(dataset)):
        if((dataset[i][kol]==indikator) and (dataset[i][4]==score)):
            a=a+1
    return a

def class_F(dataset,indikator,frekuensi,kol,JumBuy,JumNotBuy,score):
    # clas=[]
    
    # i=0
    # while(i<len(ind_arr)):
    #     clas.append([])
    #     k=0

    y=frekuensi(kol,indikator,dataset,score)
    if(score==1):
        clas=round(y/JumBuy,5)
    else:
        clas=round(y/JumNotBuy,5)
        # n=frekuensi(kol,ind_arr[i],dataset,-1)
        # clas[i].append(round(y/JumBuy,2))
        # clas[i].append(round(n/JumNotBuy,2))
        # i=i+1
    return clas




# def test(a):
#     for i in range (0,len(dataset)):
#         print(a[i])
# test(dataset[0])p,c,o,t,
def probPerX(dataset,Bar_arr,PY,PN,frekuensi,JumBuy,JumNotBuy):
    price_classY = class_F(dataset,Bar_arr[0],frekuensi,0,JumBuy,JumNotBuy,1)
    price_classN = class_F(dataset,Bar_arr[0],frekuensi,0,JumBuy,JumNotBuy,-1)
    condt_classY = class_F(dataset,Bar_arr[1],frekuensi,1,JumBuy,JumNotBuy,1)
    condt_classN = class_F(dataset,Bar_arr[1],frekuensi,1,JumBuy,JumNotBuy,-1)
    odo_classY = class_F(dataset,Bar_arr[2],frekuensi,2,JumBuy,JumNotBuy,1)
    odo_classN = class_F(dataset,Bar_arr[2],frekuensi,2,JumBuy,JumNotBuy,-1)
    trans_classY = class_F(dataset,Bar_arr[3],frekuensi,3,JumBuy,JumNotBuy,1)
    trans_classN = class_F(dataset,Bar_arr[3],frekuensi,3,JumBuy,JumNotBuy,-1)

    Y = price_classY+condt_classY+odo_classY+trans_classY
    N = price_classN+condt_classN+odo_classN+trans_classN
    if(Y>=N):
        return 1
    else:
        return -1
    

datset1 = pd.read_csv(
        'test.csv',
        delimiter=',', 
        )

dataset1=np.array(datset1)
hasilnya=[]
x=0
while(x<len(dataset1)):
    Bar_arr=dataset1[x]
    hakhir = probPerX(dataset,Bar_arr,PY,PN,frekuensi,JumBuy,JumNotBuy)
    hasilnya.append(hakhir)
    x=x+1

# print(hasilnya)

pakhir=0
nakhir=0
for i in range (0,len(hasilnya)):
    if(hasilnya[i]==1):
        pakhir=pakhir+1
    elif(hasilnya[i]==-1):
        nakhir=nakhir+1
    
pakhir=(pakhir*100)/len(hasilnya)
nakhir=(nakhir*100)/len(hasilnya)
print("positif percent",pakhir)
print("negative percent",nakhir)



nama =["positif","negatif"]
nilai =[pakhir,nakhir]

x = range(len(nama))
plt.bar(x, nilai)
plt.xticks(x, nama)

plt.ylabel('Banyak')
plt.xlabel('klasifikasi')
plt.title('Grafik Nilai')
plt.show()