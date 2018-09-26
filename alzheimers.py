import os
import csv
import numpy as np
from collections import Counter
from operator import itemgetter
import matplotlib.pyplot as plt
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
    if line[2] == "Alzheimer's disease":  # Alzheimer's disease
        if line[0] == "2016":
            y2016.append(line)
        if line[0] == "1999":
            y1999.append(line)

y2016.pop(44)
y1999.pop(44)
# print(len(y2016))
# print(len(y1999))

# print(y2016[5])
# print(y1999[5])


rot2016 = np.rot90(y2016)
rot1999 = np.rot90(y1999)

introt2016 = list(map(int, rot2016[1]))  # list(map(int, warp_list[1]))
introt1999 = list(map(int, rot1999[1]))  # list(map(int, warp_list[1]))

netRot = np.subtract(introt2016, introt1999)

# print(np.argmax(netRot))
# print(y2016[4])
# print(y1999[4])

calif = []
for line in mylist:
    if line[2] == "Alzheimer's disease":  # Alzheimer's disease
        if line[3] == "California":
            calif.append(line)

# print(len(calif))
# print(calif[5])

rotCalif = np.rot90(calif)
dead = list(map(int, rotCalif[1]))  # dead
print(dead)
print(rotCalif[5])  # year
year = list(map(int, rotCalif[5]))

year = np.flip(year, 0)
dead = np.flip(dead, 0)


def plot_increse(dead, year):
    plot_file = 'kidney.png'
    #word_tuple_list = Counter(word_appearance(content)).most_common(20)
    xs = year
    ys = dead
    xlabels = year
    plt.title("Increased in deaths of Alzheimers in California", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Frequency of deaths", fontsize=12)
    plt.xticks(xs, xlabels, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.bar(xs, ys)
    plt.savefig(plot_file)
    print("\nPlotting saved as '" + plot_file + "'.")


plot_increse(dead, year)

""" 
def plot_20_most_used_words(content):
    plot_file = 'most_used_words.png'
    word_tuple_list = Counter(word_appearance(content)).most_common(20)
    xs = range(1, 21)
    ys = [word_tuple[1] for word_tuple in word_tuple_list]
    xlabels = [word_tuple[0] for word_tuple in word_tuple_list]
    plt.title("The 20 most used words in BobRoss.txt", fontsize=16)
    plt.xlabel("Words", fontsize=12)
    plt.ylabel("Frequency of words", fontsize=12) 
    plt.xticks(xs, xlabels, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.bar(xs, ys)
    plt.savefig(plot_file)
    print("\nPlotting saved as '" + plot_file + "'.")
 """
