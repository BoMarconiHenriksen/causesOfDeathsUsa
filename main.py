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

prettyList = []
for line in mylist:
    if line[1] == 'All Causes' and line[0] == "2016":
        prettyList.append(line)

# print(prettyList[0])

# remove all the united states:
prettyList2 = prettyList.pop(44)

# print(prettyList)

warp_list = np.rot90(prettyList)


# print(warp_list)
# print(len(warp_list))
# print(warp_list[2])  # index 1 = total death, 2 = state

int_deaths = list(map(int, warp_list[1]))
print(np.argmin((int_deaths)))  # 240 #2016 : 26
# print(warp_list[2][26])
# print(warp_list[1][26])
# print(prettyList[26])


print(prettyList[1])
# print(int_deaths)
'''
# csv modulet. Husk at lave type cast, hvis float
with open(file_name) as fp:
    reader = csv.reader(fp)
    header_row = next(reader)  # hoppper over headerlinjen
    for line in reader:
        year, cause_name, state, deaths, age_adjusted, death_rate = line
        global data
        data = int(year), str(cause_name), str(state), str(
            deaths), int(age_adjusted), float(death_rate)
        # print(data)
        # new_list = []
        if data[0] == 2016:
            if data[1] == 'All Causes':
                # for number in data[4]:
                wholeList = []
                new_list = []
                for item in data_in_list:
                    new_list.append(item)
                wholeList.append(new_list)
                print(wholeList)
        # rotate_list = np.rot90(data_in_list)
        # print(rotate_list)
        # print(type(data_in_list))


# Henter data ind med numpy
# Virker ikke da kolonnerne har forskellige størrelser.
""" data = np.genfromtxt(file_name, delimiter=',',
                     dtype=np.uint16, skip_header=1, autostrip=True,) """
# print(data)
'''
