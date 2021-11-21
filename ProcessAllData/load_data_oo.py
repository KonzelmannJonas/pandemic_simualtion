import numpy as np
import matplotlib.pyplot as plt

# simulation folder
sim_folder = 'Data/8'
SIR_file = 'Data/SIR_data.npy'

# get files
SIR_array = np.load('Data/SIR_data.npy')
simulation_population = np.load('%s/population.npy' % sim_folder)

# number of time steps and interpolation translation interval
time_steps = SIR_array[0]
intpol_num = 40

# define population data from SIR
SIR_susceptible = SIR_array[1]
SIR_infected = SIR_array[2]
SIR_fatalities = SIR_array[4]
SIR_recovered = SIR_array[3]

SIR_data = [SIR_array[1], SIR_array[2], SIR_array[4], SIR_array[3]]

# get population data from Simulation
simulation_infected = np.load('%s/infected.npy' % sim_folder)
simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
simulation_susceptible = np.full(len(time_steps),
                                 len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered

simulation_data = [simulation_susceptible, simulation_infected, simulation_fatalities, simulation_recovered]

#class to process data array -> data array has to have the form: [time_steps_array, data_model1_array, data_model2_array, etc]
#data_model1_array : [suscepitble, infected, fatalities, recovered]
class PeopleToPlot():
    def __init__(self, data_array):
        self.data_array = data_array
        self.time_steps = data_array[0]
        self.interpolation_nums = []
        self.backgroundGraph = []
        self.graphColor = []
        self.graphNames = []

    # interpolate SIR and Simulation data
    def interpolate_array(self):
        for j in range(1, len(self.data_array)):
            for i in range(len(self.data_array[j])):
                index_list = np.arange(self.interpolation_nums[j-1])
                append_list = np.full(self.interpolation_nums[j-1], self.data_array[j][i][-1])
                self.data_array[j][i] = np.delete(self.data_array[j][i], index_list)
                self.data_array[j][i] = np.append(self.data_array[j][i], append_list)

    def plot(self):
        # Plot the data on three separate curves for S(t), I(t) and R(t)
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, facecolor='w', axisbelow=True)

        for j in range(1,len(self.data_array)):
            if self.backgroundGraph[j-1]:
                for i in range(len(self.data_array[j])):
                    ax.plot(self.data_array[0], self.data_array[j][i], self.graphColor[j-1][i], dashes=[8, 4], alpha=0.5, lw=2,
                            label=self.graphNames[j-1][i])
            else:
                for i in range(len(self.data_array[j])):
                    ax.plot(self.data_array[0], self.data_array[j][i], self.graphColor[j-1][i], alpha=0.5, lw=2,
                            label=self.graphNames[j-1][i])

        ax.set_xlabel('Time (d)')
        ax.set_ylabel('Number of Cases')
        # ax.set_ylim(0,1.2)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='black', lw=2, ls='-', alpha=0.25)
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        # for spine in ('top', 'right', 'bottom', 'left'):
        #    ax.spines[spine].set_visible(False)
        plt.show()

    def showData(self):
        for j in range(1,len(self.data_array)):
            for i in range(len(self.data_array[j])):
                 print("%s: %i" %(self.graphNames[j-1][i], self.data_array[j][i][-1]))


"""
graphNames = [['Sim Susceptible', 'Sim Infected', 'Sim Fatalities', 'Sim Recovered'],['SIR Susceptible', 'SIR Infected', 'SIR Fatalities', 'SIR Recovered'],['test','test','test','test']]
colors = [['blue', 'red', 'black', 'green'],['blue', 'red', 'black', 'green'],['yellow','purple','orange','grey']]
intpol_nums = [0,0,20]
background_graphs = [False,True,False]

data = [time_steps, simulation_data, SIR_data, simulation_data]

plotAllData = PeopleToPlot(data)

plotAllData.graphNames = graphNames
plotAllData.graphColor = colors
plotAllData.interpolation_nums = intpol_nums
plotAllData.backgroundGraph = background_graphs

plotAllData.interpolate_array()
plotAllData.showData()

plotAllData.plot()

"""

graphNames = [['Sim Susceptible', 'Sim Infected', 'Sim Fatalities', 'Sim Recovered'],['SIR Susceptible', 'SIR Infected', 'SIR Fatalities', 'SIR Recovered']]
colors = [['blue', 'red', 'black', 'green'],['blue', 'red', 'black', 'green']]
intpol_nums = [40,0]
background_graphs = [False, True]

data = [time_steps, simulation_data, SIR_data]

plotAllData = PeopleToPlot(data)

plotAllData.graphNames = graphNames
plotAllData.graphColor = colors
plotAllData.interpolation_nums = intpol_nums
plotAllData.backgroundGraph = background_graphs

plotAllData.interpolate_array()
plotAllData.showData()

plotAllData.plot()
