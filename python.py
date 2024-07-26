'''
#print("Hello World!!")
#print(bool())
#print(type(True))

#my_name = "Nihar"
#print(my_name.isalnum())
#print(my_name.isdigit())
#print(my_name.endswith('r'))
#print(my_name.startswith('r'))

#print(True and False)
#print(True or False)

list1 = ['hi','hello']
print(list1)
list2 = list(['hi','hello'])
print(list2)
print(len(list1))

list1.append([1,2])
list1.extend([1,2])
list1.append(3)
list1[1] = "changed"
list1.insert(1,"bruhh")
list1.pop()
list1.pop(0)
#print(list1[0])
#print(list1[1])
#print(list1[2])
print(list1[:])
print(sum(list1[4:7]))
print(list1.count(4))
print(list1.index(2))
print(list1*2)


set1 = set()
print(set1)
print(type(set1))

set1 = {'hi','hello'}
set1 = {1,2,3,4,1,2}
print(set1)
set1.add('hi')
print(set1)
set2 = {1,2,4,1,2}
print(set1.difference(set2))


dic = {1,2,3}
print(type(dic))
my_dic = {1:'one',2:'two'}
print(type(my_dic))
print(my_dic[1])

for x in my_dic:
    print(x)

for x in my_dic.values():
    print(x)

for x in my_dic.items():
    print(x)

my_dic[2] = 'three'

for x in my_dic.items():
    print(x)


tuple1 = tuple({1,2,3})
print(tuple1[0])
tuple1[0] = 4


import numpy as np

my_lst = [1,2,3,4,5]
arr = np.array(my_lst)
print(type(arr))
print(arr)
print(arr.shape)
arr[1:] = 10
print(arr)

my_lst1 = [1,2,3,4,5]
my_lst2 = [2,3,4,5,6]
my_lst3 = [3,4,5,6,7]
arr1 = np.array([my_lst1,my_lst2,my_lst3])
print(arr1)

print(arr1.shape)

arr2 = arr1.reshape(5,3)
print(arr1.shape)
print(arr2.shape)
print(arr1.reshape(1,15))
print(arr1[1:,3:])

arr3 = np.arange(1,10,step=0.5)
print(arr3)
print(np.linspace(1,100,101))

arr_new = arr
arr_new[1:] = 1000
print(arr_new)
print(arr)
arr_new1 = arr.copy()
arr_new1[1:] = 15
print(arr_new1)
print(arr)
print(arr[arr>10])

print(np.ones((5),dtype=int))

random = np.random.rand(5,5)
print(random)
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,20).reshape(5,4),index = ['row1','row2','row3','row4','row5'],columns=['column1','column2','column3','column4'])
print(df.head())
print(df.to_csv('test1.csv'))

print(df.loc['row1'])
print(df.iloc[1:3,0])
print(type(df.iloc[1:3,1:3]))
print(type(df.iloc[1:3,1]))

print(df.iloc[:,:].values.shape)

print(df.isnull().sum())

print(df['column1'].value_counts())

print(df['column1'].is_unique)

print(df[['column1','column2']])

