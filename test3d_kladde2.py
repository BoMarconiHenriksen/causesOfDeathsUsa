import os
import csv
import numpy as np
from collections import Counter
from operator import itemgetter
import matplotlib.pyplot as plt

import testLoadData

file_name = 'NCHS_-_Leading_Causes_of_Death__United_States.csv'

alzheimers = testLoadData.load_death_data(file_name, {"Alzheimer's disease": 2}, {"United States": 3})
    # dimension index 0 == 51 (antal stater i datasætter == 51 == len(alzheimers)/18.)
    # dimension index 1 == 18 (der er 18 år i datasættet.) 
    # dimension index 2 == 6 (der er 6 categorier i hver entry)

nptotal = np.array(alzheimers).reshape(51, 18, 6)
nptotal = np.flip(nptotal, axis = 1) 
        # flipper dataerne i årenes akse, så årene går fra gamle til nye
        # (årene ligger i dimension index 1)


#tager alle døds tallene i en 2d array og laver dem om til integers:
# (dødstallene ligger i dimension index 2, index 4)
death2d = nptotal[:,:,4].astype(int)
#tager forskellen mellem dødstalene fra år til år for hver stat
diff2d = np.diff(death2d, n=1, axis=1)
# summer forskellene == returnere en 1d array af forskellen fra 1999 til 2016 for hver stat
net_diff1d = np.sum(diff2d, axis=1)


print("the deaths differences for each state:")
print(net_diff1d)
state_index = np.argmax(net_diff1d) #the index of the state (in dimension 0)

print("the name of the state with the highest death difference:")
print(nptotal[state_index,:,:][0][3]) #print the name of the state as a string

print("the difference in death:")
print(net_diff1d[state_index]) #print the difference in deaths

print("the death toll each year for that state:")
print(death2d[state_index]) #print the death toll for each year

print("the years covered")
print(nptotal[:,:,0][0].astype(int)) #print each year





'''
#   ----------- nptotal -------------
# 1st dimension == info from each state, for example: 
#['1999' "Alzheimer's disease (G30)" "Alzheimer's disease" 'Alabama' '772' '17.80']
#['2000' "Alzheimer's disease (G30)" "Alzheimer's disease" 'Alabama' '895' '20.40']
#['2016' "Alzheimer's disease (G30)" "Alzheimer's disease" 'Alabama' '2507' '45.00']
#18
print(nptotal[0,:,:][0]) 
print(nptotal[0,:,:][1]) 
print(nptotal[0,:,:][17]) 
print(len(nptotal[0,:,:])) 
print("***")
# 2nd dimension == info from each year:
#['1999' "Alzheimer's disease (G30)" "Alzheimer's disease" 'Alabama' '772' '17.80']
#['1999' "Alzheimer's disease (G30)" "Alzheimer's disease" 'Alaska' '24' '11.90']
#['1999' "Alzheimer's disease (G30)" "Alzheimer's disease" 'Wyoming' '103' '23.90']
#51
print(nptotal[:,0,:][0])
print(nptotal[:,0,:][1])
print(nptotal[:,0,:][50])
print(len(nptotal[:,0,:]))
print("***")
# 3rd dimension == info from each cell:
#['1999' '2000' '2001' '2002' '2003' '2004' '2005' '2006' '2007' '2008'
# '2009' '2010' '2011' '2012' '2013' '2014' '2015' '2016']
#51
print(nptotal[:,:,0][0])
print(len(nptotal[:,:,0]))
'''