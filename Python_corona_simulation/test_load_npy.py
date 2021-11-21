import numpy as np

num_files = 24
pop_data = np.zeros((3,num_files))


for j in range(num_files):
    current_num = int(j*10)
    population = np.load('pop_data/population_%i.npy' % current_num)

    infected = 0
    recovered = 0
    fatalities = 0

    for i in population[:,6]:
        if i == 1:
            infected += 1
        elif i== 2:
            recovered +=1
        elif i == 3:
            fatalities += 1

    pop_data[0][j] = infected
    pop_data[1][j] = recovered
    pop_data[2][j] = fatalities


for i in range(len(pop_data)):
    print(pop_data[i][num_files-1])

#print(pop_data)
#print(infected)
#print("Infected: %i" %num_inf)
#print(population[:,6])
#print(population)
