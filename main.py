import os
import csv
import numpy as np
file_name = 'NCHS_-_Leading_Causes_of_Death__United_States.csv'
# from downloader import download

# https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD
# https://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv
# url = 'https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD'
# file_name = os.path.basename(url)
# download(url, file_name)

# csv modulet. Husk at lave type cast, hvis float
with open(file_name) as fp:
    reader = csv.reader(fp)
    header_row = next(reader)  # hoppper over headerlinjen
    for line in reader:
        year, cause_name, state, deaths, age_adjusted, death_rate = line
        data = int(year), str(cause_name), str(state), str(
            deaths), int(age_adjusted), float(death_rate)
        # print(data)

# Henter data ind med numpy
# Virker ikke da kolonnerne har forskellige størrelser.
""" data = np.genfromtxt(file_name, delimiter=',',
                     dtype=np.uint16, skip_header=1, autostrip=True,) """
print(data)
