
import numpy as np

arr1 = ["2016", "bla", "Alzheimer's disease", "Louisiana", 2195, 45.00]
arr2 = ["2015", "bla", "Alzheimer's disease", "Louisiana", 2018, 42.50]
arr3 = ["2014", "bla", "Alzheimer's disease", "Louisiana", 1670, 36.00]
arr3b = ["2013","bla","Alzheimer's disease","Louisiana",1505,32.90]
arr4 = ["2016", "bla", "Alzheimer's disease", "Maine", 577, 29.60]
arr5 = ["2015", "bla", "Alzheimer's disease", "Maine", 544, 28.40]
arr6 = ["2014", "bla", "Alzheimer's disease", "Maine", 434, 22.70]
arr6b = ["2013","bla", "Alzheimer's disease", "Maine",401,21.60]
arr7 = ["2016", "bla", "Alzheimer's disease", "Maryland", 1178, 17.40]
arr8 = ["2015", "bla", "Alzheimer's disease", "Maryland", 1095, 16.40]
arr9 = ["2014", "bla", "Alzheimer's disease", "Maryland", 934, 14.50]
arr9b = ["2013","bla","Alzheimer's disease","Maryland",919,14.30]

total = [arr1, arr2, arr3, arr3b, arr4, arr5, arr6, arr6b, arr7, arr8, arr9, arr9b]

nptotal = np.array(total).reshape(3,4,6)
nptotal = np.flip(nptotal, axis = 1) #flipped, so that the years go from old to new

'''
# dimension 0 = info from each state, for example: 
#[['2014' 'bla' "Alzheimer's disease" 'Louisiana' '1670' '36.0']
# ['2015' 'bla' "Alzheimer's disease" 'Louisiana' '2018' '42.5']
# ['2016' 'bla' "Alzheimer's disease" 'Louisiana' '2195' '45.0']]
print(nptotal[0,:,:]) 
print("***")
#dimension 1 = info from each year:
#[['2014' 'bla' "Alzheimer's disease" 'Louisiana' '1670' '36.0']
# ['2014' 'bla' "Alzheimer's disease" 'Maine' '434' '22.7']
# ['2014' 'bla' "Alzheimer's disease" 'Maryland' '934' '14.5']]
print(nptotal[:,0,:])
print("***")
#dimension 2 = info from each cell:
#[['2014' '2015' '2016']
# ['2014' '2015' '2016']
# ['2014' '2015' '2016']]
print(nptotal[:,:,3])
'''


#tager alle døds tallene i en 2d array og laver dem om til integers:
death2d = (nptotal[:,:,4]).astype(int)
print(death2d)
nr2 = np.diff(death2d, n=1, axis=1)
print(nr2)
nr3 = np.sum(nr2, axis=1)
print(nr3)
nr4 = np.argmax(nr3) #the index of the state (in dimension 0)
print(nptotal[nr4,:,:][0][3]) #print the name of the state as a string
print(nr3[nr4]) #print the difference in deaths
print(death2d[nr4]) #print the death toll for each year
print(nptotal[:,:,0][0].astype(int)) #print each year
