import numpy as np

data_folder = 'data/16'
infected_file_name = '%s/infected.npy'%data_folder
deaths_file_name = '%s/fatalities.npy'%data_folder

infected = np.load(infected_file_name)
deaths = np.load(deaths_file_name)


biggest_infected_value = 0
for i in infected:
    if i > biggest_infected_value:
        biggest_infected_value = i

'''
biggest_deaths_value = 0
for i in deaths:
    if i > biggest_deaths_value:
        biggest_deaths_value = i
'''
biggest_deaths_value = deaths[-1]

print('File: ', data_folder)
print('Most Infected: ', biggest_infected_value)
print('Most Deaths: ', biggest_deaths_value)
