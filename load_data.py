''' 
This class is used to convert the csv file to a list and
get the right data for each task.
'''

import csv

#must_have == dictionary of items each line must contain
#cant_have == dictionary of items each line must not contain
def load_death_data(file_name, must_have, cant_have):
    raw_data = []
    with open(file_name) as fp:
        reader = csv.reader(fp)
        raw_data = list(reader)

    final_data = [] #only lines that contain needed element
    for line in raw_data:
        # k er state, v er index nr.
        # all() tager en liste af booleans og returnere true hvis alle booleans er true.
        if (all([line[v] == k for k, v in must_have.items()]) and 
            all([line[v] != k for k, v in cant_have.items()])):
            final_data.append(line)
    return final_data
