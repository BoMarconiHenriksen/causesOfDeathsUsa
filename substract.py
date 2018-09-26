import os
import csv
import numpy as np
from collections import Counter
from operator import itemgetter
file_name = 'NCHS_-_Leading_Causes_of_Death__United_States.csv'
# from downloader import download

# https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD
# https://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv
# url = 'https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD'
# file_name = os.path.basename(url)
# download(url, file_name)
mylist = []
with open(file_name) as fp:
    reader = csv.reader(fp)
    mylist = list(reader)
# print(mylist)

y2016 = []
y1999 = []
for line in mylist:
    if line[1] == 'All Causes':
        if line[0] == "2016":
            y2016.append(line)
        if line[0] == "1999":
            y1999.append(line)

# print(len(y2016))
# print(len(y1999))

# print(y2016[5])
# print(y1999[5])

rot2016 = np.rot90(y2016)
rot1999 = np.rot90(y1999)

introt2016 = list(map(int, rot2016[1]))  # list(map(int, warp_list[1]))
introt1999 = list(map(int, rot1999[1]))  # list(map(int, warp_list[1]))
# print(rot2016[1])
netRot = np.subtract(introt2016, introt1999)
# print(netRot)
netRotPos = netRot.clip(0)
# print(netRotPos)

a = np.positive(netRotPos)
b = netRotPos[np.nonzero(a)]

smallestGrowth = np.sort(b)[0]
reformat = np.array(netRot)

ourIndex = list(reformat).index(smallestGrowth)
print(ourIndex)


'''
tmp = [1,2,3,4,5] #python list
a = numpy.array(tmp) #numpy array
i = list(a).index(2) # i will return index of 2, which is 1
'''

print(y1999[ourIndex])
print(y2016[ourIndex])
