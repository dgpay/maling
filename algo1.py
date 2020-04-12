import string 
import csv
import numpy as np
import pandas as pd

# from sklearn.cluster import KMeans
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import MinMaxScaler
# import seaborn as sns
import matplotlib.pyplot as plt



dataset = pd.read_csv(
        '1.csv',
        delimiter=';', 
        )
dataset1= pd.read_csv(
        '1.csv',
        delimiter=';', 
        )

print(dataset.head())
print("\n")
print(dataset.columns.values)

dataset.isna().head()
print(dataset.isna().sum())


dataset = dataset.drop(["id","year","long", "lat","state","description","county", "transmission","vin" ,"drive","size"	,"type"	,"paint_color"	,"image_url","url",	"region","region_url","manufacturer","model","condition","cylinders","fuel","title_status"], axis = 1)
dataset1= dataset1.drop(["no","long", "lat","state","description","county","drive","image_url","url","paint_color"	,"vin","region","region_url","size","manufacturer","model","cylinders","fuel"], axis = 1)
print("id	price	year	condition	odometer	title_status	transmission	type")
print(dataset1.columns.values)

print(dataset.head())
print(dataset1.head())

dt = dataset.iloc[:, 1:3]
det=dataset1.iloc[:,1:16]
print(dt.head())

dt = dt.apply (pd.to_numeric, errors='coerce')
dt = dt.dropna()
det=det.dropna()
print(dt.isna().sum())
print(det.isna().sum())
print(len(det))
# arr=dt.to_numpy()
# col1=arr[:,[0]]
# col2=arr[:,[1]]
# col3=arr[:,[2]]
# col4=arr[:,[3]]
# i=0
# c1=[]
# c2=[]
# c3=[]
# c4=[]
# print(len(col1))
# while(i<len(col1)):
#     c1.append(col1[i])
#     c2.append(col2[i])
#     c3.append(col3[i])
#     c4.append(col4[i])
#     i=i+1

#dict = {'id':dt.id,'price':dt.price,'year':dt.year,'odometer':dt.odometer}  
dict = {'price':dt.loc[: , "price"],'odometer':dt.loc[: , "odometer"]}  

df = pd.DataFrame(dict) 
df.to_csv('datset.csv') 



det['split'] = np.random.randn(det.shape[0], 1)

msk = np.random.rand(len(det)) <= 0.7

train = det[msk]
test = det[~msk]
print(train)
print(test)
df = pd.DataFrame(train) 
df.to_csv('train.csv') 
df = pd.DataFrame(test) 
df.to_csv('test.csv') 
print(len(dt))