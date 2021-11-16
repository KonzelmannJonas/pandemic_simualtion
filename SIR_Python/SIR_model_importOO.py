from SIR_model_oo import SIR_simulation

# Total population
pop_size = 2000

# Initial number of infected and recovered individuals, I0 and R0.
I0 = 1
R0 = 0
D0 = 0
initNums = [I0, R0, D0]

# Contact rate, beta, and mean recovery rate, gamma, (in 1/days), death rate delta
beta = 0.5
gamma = 1. / 22
delta = 0.01
rates = [beta, gamma, delta]
# A grid of time points (in days)
num_of_days = 160

sim = SIR_simulation(pop_size, initNums, rates, num_of_days)
sim.save_file_name = '3_SIR_folder/3_SIR_data.npy'
sim.getValues()
#sim.safeData()
sim.save_parameters()

print('Most Death', sim.getHighest(sim.D))
print('Most Infected: ', sim.getHighest(sim.I))

sim.plot()


