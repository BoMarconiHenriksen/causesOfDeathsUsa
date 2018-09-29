
import numpy as np
import testLoadData

file_name = 'NCHS_-_Leading_Causes_of_Death__United_States.csv'

# Task 1: Which state has the most deaths in the year of 2016? (All causes)
def task_1(file_name):
    clean_list = testLoadData.load_death_data(file_name, {"2016": 0, "All causes": 2}, {"United States": 3})
    gross_2darr = np.array(clean_list).reshape(51,6)
    death_counts = gross_2darr[:,4].astype(int)                         # number of deaths - 2d array of ints
    state_index = np.argmax(death_counts)
    return ("Task 1: state: " + gross_2darr[state_index,3] + 
            " death count 2016: " + gross_2darr[state_index,4])

# Task 2: Which state has the least deaths in the year of 2016? (All causes)
def task_2(file_name):
    useable_data = testLoadData.load_death_data(file_name, {"2016": 0, "All causes": 2}, {"United States": 3})
    gross_2darr = np.array(useable_data).reshape(51,6)
    death_counts = gross_2darr[:,4].astype(int)                         # number of deaths - 2d array of ints
    state_index = np.argmin(death_counts)
    return ("Task 2: state: " + gross_2darr[state_index,3] + 
            " death count 2016: " + gross_2darr[state_index,4])

# Task 3: Which state has had the smallest increase in deaths from 1999-2016? (All causes)
def task_3(file_name):
    useable_data = testLoadData.load_death_data(file_name, {"All causes": 2}, {"United States": 3})
    gross_3darr = np.array(useable_data).reshape(51, 18, 6)
    gross_3darr = np.flip(gross_3darr, axis = 1)                        # flip the years, earliest are now first
    death_counts = gross_3darr[:,:,4].astype(int)                       # number of deaths - 2d array of ints
    death_diff_yearly = np.diff(death_counts, n=1, axis=1)
    death_diff_period = np.sum(death_diff_yearly, axis=1)               # total difference in deaths across the era for each state
    smallest_positive = min(i for i in death_diff_period if i > 0)
    state_index = list(death_diff_period).index(smallest_positive)
    return ("Task 3: state: " + gross_3darr[state_index,0,3] + 
            " death count increase: " + str(death_diff_period[state_index])) 

# Task 4: Which state has the most deaths caused by kidney disease in the year of 2005?
def task_4(file_name):
    useable_data = testLoadData.load_death_data(file_name, {"2005": 0, "Kidney disease": 2}, {"United States": 3})
    gross_2darr = np.array(useable_data).reshape(51,6)
    death_counts = gross_2darr[:,4].astype(int)                     # number of deaths - 2d array of ints
    state_index = np.argmax(death_counts)
    return ("Task 4: state: " + gross_2darr[state_index,3] + 
            " kidney death count: " + gross_2darr[state_index,4])

# Task 5: Which state has had the biggest increase in the death of Alzheimers from 1999-2016? 
#         Plot the increase year for year using matplotlib
def task_5(file_name):
    useable_data = testLoadData.load_death_data(file_name, {"Alzheimer's disease": 2}, {"United States": 3})
    gross_3darr = np.array(useable_data).reshape(51, 18, 6)
    gross_3darr = np.flip(gross_3darr, axis = 1)                            # flip the years, earliest are now first
    death_counts = gross_3darr[:,:,4].astype(int)                           # number of deaths - 2d array of ints
    death_diff_yearly = np.diff(death_counts, n=1, axis=1)          
    death_diff_period = np.sum(death_diff_yearly, axis=1)                   # total difference in deaths across the era for each state
    state_index = np.argmax(death_diff_period)

    diff_yearly_adjusted = np.insert(death_diff_yearly[state_index], 0, 0)  # add a zero at the beginning, so that the death difference 
    year_list = gross_3darr[:,:,0][state_index].astype(int)                 #       is a comparrison to the previous year (the first year is the beginning, 
    state_name = gross_3darr[:,:,3][state_index][0]                         #       and thus there is no difference from the precious year).
    
    testLoadData.plot_increse(diff_yearly_adjusted, year_list, state_name)
    return ("Task 5: state: " + gross_3darr[state_index,0,3] + 
            " alzheimers death count increase: " + str(death_diff_period[state_index])) 

print(task_1(file_name))
print(task_2(file_name))
print(task_3(file_name))
print(task_4(file_name))
print(task_5(file_name))