
'''
This class has the solutions for all the tasks for this assignment.
'''
import numpy as np
import load_data
import plotting


# Task 1: Which state has the most deaths in the year of 2016? (All causes)
def task_1(file_name):
    deaths_in_each_state_in_2016_list = load_data.load_death_data(
        file_name, {"2016": 0, "All causes": 2}, {"United States": 3})

    # [ [alabama info], [Alaska info], [California info], ect ]
    deaths_in_each_state_2d_array = np.array(
        deaths_in_each_state_in_2016_list).reshape(51, 6)

    # A list that contains only the number of deaths for each state in 2016
    death_counts = deaths_in_each_state_2d_array[:, 4].astype(int)

    # The index number of the max number of deaths
    state_index = np.argmax(death_counts)

    return ("Task 1: state: " + deaths_in_each_state_2d_array[state_index, 3] +
            " death count 2016: " + deaths_in_each_state_2d_array[state_index, 4])


# Task 2: Which state has the least deaths in the year of 2016? (All causes)
def task_2(file_name):
    deaths_in_each_state_in_2016_list = load_data.load_death_data(
        file_name, {"2016": 0, "All causes": 2}, {"United States": 3})

    # [ [alabama info], [Alaska info], [California info], ect ]
    deaths_in_each_state_2d_array = np.array(
        deaths_in_each_state_in_2016_list).reshape(51, 6)

    # A list that contains only the number of deaths for each state in 2016
    death_counts = deaths_in_each_state_2d_array[:, 4].astype(int)

    # argmin findes the lowest number in the list
    state_index = np.argmin(death_counts)

    return ("Task 2: state: " + deaths_in_each_state_2d_array[state_index, 3] +
            " death count 2016: " + deaths_in_each_state_2d_array[state_index, 4])


# Task 3: Which state has had the smallest increase in deaths from 1999-2016? (All causes)
def task_3(file_name):
    deaths_from_1999_to_2016 = load_data.load_death_data(
        file_name, {"All causes": 2}, {"United States": 3})

    # 3d array
    death_in_each_state_3d_array = np.array(
        deaths_from_1999_to_2016).reshape(51, 18, 6)

    # flip the years, earliest are now first
    death_in_each_state_3d_array = np.flip(
        death_in_each_state_3d_array, axis=1)

    # number of deaths - 2d array of ints
    death_counts = death_in_each_state_3d_array[:, :, 4].astype(int)
    death_diff_yearly = np.diff(death_counts, n=1, axis=1)

    # total difference in deaths across the era for each state in a np array
    death_diff_period = np.sum(death_diff_yearly, axis=1)

    smallest_positive = min(i for i in death_diff_period if i > 0)

    # np array knoverters til en list
    state_index = list(death_diff_period).index(smallest_positive)

    return ("Task 3: state: " + death_in_each_state_3d_array[state_index, 0, 3] +
            " death count increase: " + str(death_diff_period[state_index]))


# Task 4: Which state has the most deaths caused by kidney disease in the year of 2005?
def task_4(file_name):
    deaths_by_kidney_disease_2005 = load_data.load_death_data(
        file_name, {"2005": 0, "Kidney disease": 2}, {"United States": 3})

    # 2d array with deaths by kidney disease in the year 2005
    deaths_kidney_disease_2d_array = np.array(deaths_by_kidney_disease_2005).reshape(51, 6)

    # number of deaths - 1d array of ints
    death_counts = deaths_kidney_disease_2d_array[:, 4].astype(int)
    
    state_index = np.argmax(death_counts)

    return ("Task 4: state: " + deaths_kidney_disease_2d_array[state_index, 3] +
            " kidney death count: " + deaths_kidney_disease_2d_array[state_index, 4])


# Task 5: Which state has had the biggest increase in the death of Alzheimers from 1999-2016?
#         Plot the increase year for year using matplotlib
def task_5(file_name):
    useable_data = load_data.load_death_data(
        file_name, {"Alzheimer's disease": 2}, {"United States": 3})

    deaths_by_alzheimers_3d_array = np.array(useable_data).reshape(51, 18, 6)

    # flip the years, earliest are now first
    deaths_by_alzheimers_3d_array = np.flip(deaths_by_alzheimers_3d_array, axis=1)

    # number of deaths - 2d array of ints
    death_counts = deaths_by_alzheimers_3d_array[:, :, 4].astype(int)
    death_diff_yearly = np.diff(death_counts, n=1, axis=1)

    # total difference in deaths across the era for each state
    death_diff_period = np.sum(death_diff_yearly, axis=1)
    state_index = np.argmax(death_diff_period)

    # add a zero at the beginning, so that the death difference
    # is a comparrison to the previous year (the first year is the beginning,
    # and thus there is no difference from the previous year).
    diff_yearly_adjusted = np.insert(death_diff_yearly[state_index], 0, 0)
    year_list = deaths_by_alzheimers_3d_array[:, :, 0][state_index].astype(int)
    state_name = deaths_by_alzheimers_3d_array[:, :, 3][state_index][0]

    plotting.plot_increse(diff_yearly_adjusted, year_list, state_name)

    return ("Task 5: state: " + deaths_by_alzheimers_3d_array[state_index, 0, 3] +
            " alzheimers death count increase: " + str(death_diff_period[state_index]))
