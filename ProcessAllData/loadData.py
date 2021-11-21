import numpy as np
import matplotlib.pyplot as plt

# simulation folder
sim_folder = 'Data/8'
SIR_file = 'Data/SIR_data.npy'

# get files
SIR_data = np.load('Data/SIR_data.npy')
simulation_population = np.load('%s/population.npy' % sim_folder)

# number of time steps and interpolation translation interval
time_steps = SIR_data[0]
intpol_num = 40

# define population data from SIR
SIR_susceptible = SIR_data[1]
SIR_infected = SIR_data[2]
SIR_recovered = SIR_data[3]
SIR_fatalities = SIR_data[4]

# get population data from Simulation
simulation_infected = np.load('%s/infected.npy' % sim_folder)
simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
simulation_susceptible = np.full(len(time_steps), len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered


# interpolate SIR and Simulation data
def interpolate_array(array, interpolate_num):
    index_list = np.arange(interpolate_num)
    append_list = np.full(interpolate_num, array[-1])
    array = np.delete(array, index_list)
    array = np.append(array, append_list)
    return array


# interpolate all simulation data
simulation_infected_interpolated = interpolate_array(simulation_infected, intpol_num)
simulation_susceptible_interpolated = interpolate_array(simulation_susceptible, intpol_num)
simulation_fatalities_interpolated = interpolate_array(simulation_fatalities, intpol_num)
simulation_recovered_interpolated = interpolate_array(simulation_recovered, intpol_num)

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='w', axisbelow=True)

ax.plot(time_steps, SIR_susceptible, 'b', dashes=[8, 4], alpha=0.5, lw=2, label='SIR Susceptible')
ax.plot(time_steps, simulation_susceptible_interpolated, 'b', alpha=0.5, lw=2, label='Simulation Susceptible')

ax.plot(time_steps, SIR_infected, 'r', dashes=[8, 4], alpha=0.5, lw=2, label='SIR Infected')
ax.plot(time_steps, simulation_infected_interpolated, 'r', alpha=0.5, lw=2, label='Simulation Infected')

ax.plot(time_steps, SIR_recovered, 'g', dashes=[8, 4], alpha=0.5, lw=2, label='SIR Recovered')
ax.plot(time_steps, simulation_recovered_interpolated, 'g', alpha=0.5, lw=2, label='Simulation Recovered')

ax.plot(time_steps, SIR_fatalities, 'purple', dashes=[8, 4], alpha=0.5, lw=2, label='SIR Fatalities')
ax.plot(time_steps, simulation_fatalities_interpolated, 'purple', alpha=0.5, lw=2, label='Simulation Fatalities')

ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
# ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='black', lw=2, ls='-', alpha=0.25)
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
# for spine in ('top', 'right', 'bottom', 'left'):
#    ax.spines[spine].set_visible(False)
plt.show()

print(simulation_susceptible[-1],simulation_infected[-1],simulation_recovered[-1],simulation_fatalities[-1])
