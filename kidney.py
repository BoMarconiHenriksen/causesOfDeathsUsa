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

y2005 = []
for line in mylist:
    if line[2] == 'Kidney disease':
        if line[0] == "2005":
            y2005.append(line)

# print(len(y2005))
# print(y2005[44])

y2005.pop(44)
# print(len(y2005))

rotate2005 = np.rot90(y2005)
dead = rotate2005[1]
# print(type(dead[5]))


deadint = list(map(int, dead))  # list(map(int, warp_list[1]))
# print(np.argmax((deadint)))  # index 38
print(y2005[38])
print(np.sort(deadint))
