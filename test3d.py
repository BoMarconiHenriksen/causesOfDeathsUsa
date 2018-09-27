# 2018-09-27 kl. 11.00 -- test af numpy 3d arrays

#1999,Alzheimer's disease (G30),Alzheimer's disease,Louisiana,683,17.90
#2016,Alzheimer's disease (G30),Alzheimer's disease,Maine,577,29.60

import numpy as np

arr1 = ["2016", "bla", "Alzheimer's disease", "Louisiana", 2195, 45.00]
arr2 = ["2015", "bla", "Alzheimer's disease", "Louisiana", 2018, 42.50]
arr3 = ["2014", "bla", "Alzheimer's disease", "Louisiana", 1670, 36.00]
arr4 = ["2016", "bla", "Alzheimer's disease", "Maine", 577, 29.60]
arr5 = ["2015", "bla", "Alzheimer's disease", "Maine", 544, 28.40]
arr6 = ["2014", "bla", "Alzheimer's disease", "Maine", 434, 22.70]
arr7 = ["2016", "bla", "Alzheimer's disease", "Maryland", 1178, 17.40]
arr8 = ["2015", "bla", "Alzheimer's disease", "Maryland", 1095, 16.40]
arr9 = ["2014", "bla", "Alzheimer's disease", "Maryland", 934, 14.50]

total = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]

newtotal = np.array(total)

nr2 = newtotal.reshape(3,3,6)

'''
print(nr2)
print("****")
print(nr2[1,:,:]) #hver stat (1 er Maryland)
print("****")
print(nr2[:,1,:]) #hvert år (1 er 2015)
print("****")
print(nr2[:,:,1]) #hver categori (1 er blabla)
'''

#print(nr2[:,:,4])
nr3 = np.flip(nr2[:,:,4], axis=1).astype(int)
#print(nr3)

nr4 = np.diff(nr3, n=1, axis=1)
#print(nr4)

nr5 = np.sum(nr4, axis=1)
nr6 = np.argmax(nr5)  #nr6 (index 0) == Luisiana

difference = nr5[nr6]
years = nr2[nr6,:,0]
deaths = nr2[nr6,:,4]
name = nr2[nr6,0,3]

print(difference)
print(years)
print(deaths)
print(name)

