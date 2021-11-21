import numpy as np
import matplotlib.pyplot as plt

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

