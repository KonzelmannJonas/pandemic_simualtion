import numpy as np
import matplotlib.pyplot as plt

# class to process data array -> data array has to have the form: [time_steps_array, data_model1_array, data_model2_array, etc]
# data_model1_array : [suscepitble, infected, fatalities, recovered] or other variations if neede like: [infected, fatalities]
class PeopleToPlot():
    def __init__(self, data_array):
        self.data_array = data_array
        self.time_steps = data_array[0]
        self.interpolation_nums = []
        self.backgroundGraph = []
        self.graphColor = []
        self.graphNames = []

        # variables to cut data to the right lentgh later
        self.graph_length = 0
        self.pop_indexes = []

    # interpolate SIR and Simulation data
    def interpolate_array(self):
        for j in range(1, len(self.data_array)):
            current_array = []
            for i in range(len(self.data_array[j])):
                index_list = np.arange(self.interpolation_nums[j - 1])
                append_list = np.full(self.interpolation_nums[j - 1], self.data_array[j][i][-1])
                list_at_the_moment = np.delete(self.data_array[j][i], index_list)
                list_at_the_moment = np.append(list_at_the_moment, append_list)
                current_array.append(list_at_the_moment)
            self.data_array[j] = current_array

    # cut all graphs to model length of specific given array in data_array
    def cutGraphs(self, model_array):
        self.graph_length = len(self.data_array[model_array][0])
        self.time_steps = self.time_steps[0:(self.graph_length)]

        for j in range(1, len(self.data_array)):
            current_array = []
            if j != model_array:
                for i in range(len(self.data_array[j])):
                    current_array.append(
                        self.data_array[j][i][(self.pop_indexes[j - 1]):(self.pop_indexes[j - 1] + self.graph_length)])
            if current_array != []:
                self.data_array[j] = current_array

    def plot(self):
        # Plot the data on three separate curves for S(t), I(t) and R(t)
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, facecolor='w', axisbelow=True)

        for j in range(1, len(self.data_array)):
            if self.backgroundGraph[j - 1]:
                for i in range(len(self.data_array[j])):
                    ax.plot(self.time_steps, self.data_array[j][i], self.graphColor[j - 1][i], dashes=[8, 4], alpha=0.5,
                            lw=2,
                            label=self.graphNames[j - 1][i])
            else:
                for i in range(len(self.data_array[j])):
                    ax.plot(self.time_steps, self.data_array[j][i], self.graphColor[j - 1][i], alpha=0.5, lw=2,
                            label=self.graphNames[j - 1][i])

        ax.set_xlabel('Zeit (d)')
        ax.set_ylabel('Anzahl Infizierte/Todesfälle')
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
        for j in range(1, len(self.data_array)):
            for i in range(len(self.data_array[j])):
                print("%s: %i" % (self.graphNames[j - 1][i], self.data_array[j][i][-1]))

