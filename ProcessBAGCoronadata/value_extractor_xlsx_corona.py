import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np

xlsx_file = Path('xlsxData', '200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx')


class ProcessorXlsx():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_ws = pd.read_excel(file_path)  # excel file
        self.cols_to_extract = [1, 5]  # columns out of excel file to get values from
        self.extracted_data = []  # array to dump data in
        self.cut_cols = True  # whether to cut off the first couple items becauase they don't contain values
        self.cut_cols_num = 6  # how many items in the front that are removed
        self.chop_array = 0  # 0=no chop, 1=chop befor index, 2 = chop after index
        self.chop_array_index = 100  # index to chop array
        self.legend_names = ['Infizierte', 'Todesfälle']  # ,'hospitalizations' if needed
        self.graph_colors = ['green', 'black']  # ,'green' for hospitalizations
        self.time_steps = []
        self.save_file_name = 'UseableCoronaData/index0_corona_data.npy'  # file to safe data to

        self.swiss_pop_total = 8725705
        self.shorten_num = 100000  # "cases per shorten num" e.g 120 cases per 100'000

        self.box_pts = 0  # length of boxes convolved
        self.data_to_flat = [0]  # list containing indexes of Graphs that will be flattened

    # write demanded values to extracted_data to make it workable + cut off unnecessary parts
    def extractValues(self):
        for i in self.cols_to_extract:
            current_col = self.data_ws.iloc[:, i]
            if self.cut_cols:
                current_col = current_col[self.cut_cols_num:]
            if self.chop_array == 1:
                current_col = current_col[self.chop_array_index:]
            if self.chop_array == 2:
                current_col = current_col[:self.chop_array_index]
            self.extracted_data.append(current_col)

        self.time_steps = np.arange(len(self.extracted_data[0]))

    # refactor graph to "cases per self.shorten_num" , e.g. 5 cases per 100'000 people
    def shortenGraph(self):
        for i in range(len(self.extracted_data)):
            shorten_factor = self.swiss_pop_total / self.shorten_num  # factor to shorten the array items later on
            self.extracted_data[i] = [xi / shorten_factor for xi in self.extracted_data[i]]

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel('Zeit[d]')
        ax.set_ylabel('Infizierte/Todesfälle Anzahl')
        ax.grid(b=True, which='major', c='black', lw=2, ls='-', alpha=0.25)
        for i in range(len(self.extracted_data)):
            ax.plot(self.time_steps, self.extracted_data[i], label=self.legend_names[i], color=self.graph_colors[i])
        ax.legend()
        plt.show()

    # saves the data to a specific file
    def saveData(self):
        np.save(self.save_file_name, self.extracted_data)

    # flaten the Graph with np.convolve
    def flatenGraph(self):
        box = np.ones(self.box_pts) / self.box_pts
        for i in self.data_to_flat:
            self.extracted_data[i] = np.convolve(self.extracted_data[i], box, mode='same')

    # get highest Value in specific Interval, interval: [low, high], data_asked: 0=cases, 1=deaths
    def getHighestPoint(self, interval, data_asked):
        highest_value = 0
        for i in range(interval[0], interval[1]):
            if self.extracted_data[data_asked][i] > highest_value:
                highest_value = self.extracted_data[data_asked][i]
        return highest_value

    """
        def chopDataArray(self, index_to_cut, chop_after_index=True):
            if chop_after_index:
                index_list_chop = np.arange(index_to_cut,len(self.extracted_data[0]))
            elif not chop_after_index:
                index_list_chop = np.arange(index_to_cut)
            for i in range(len(self.extracted_data)):
                self.extracted_data[i] = np.delete(self.extracted_data[i],index_list_chop)
    """


# First Wave has length of about 200 days -> used in WorkWithData

xlsxdata_obj = ProcessorXlsx(xlsx_file)
xlsxdata_obj.chop_array = 2 #how to chop array -> 0=nothing 1=chop before array 2=chop after array
xlsxdata_obj.chop_array_index = 200
xlsxdata_obj.save_file_name = 'UseableCoronaData/index2_corona_data.npy'
xlsxdata_obj.shorten_num = 100000
xlsxdata_obj.box_pts = 4

xlsxdata_obj.extractValues()
#xlsxdata_obj.flatenGraph()

# xlsxdata_obj.shortenGraph()

#print('Most Infected: ', xlsxdata_obj.getHighestPoint([0, 100], 0))
#print('Most Death: ', xlsxdata_obj.getHighestPoint([0, 100], 1))
# print(len(xlsxdata_obj.extracted_data[0]))
print(type(xlsxdata_obj.extracted_data[1]))

xlsxdata_obj.plot()
xlsxdata_obj.saveData()
