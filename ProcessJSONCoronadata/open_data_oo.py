import json
import numpy as np
import matplotlib.pyplot as plt
import random
import keyboard

#file path
EU_data_file = 'CoronavirusData/EU_coronavirus_data.json'

#open data file
with open(EU_data_file) as json_file:
    EU_data_dict = json.load(json_file)['records']

#get list of country shortcuts
countries = []
for i in EU_data_dict:
    if i['countryterritoryCode'] not in countries:
        countries.append(i['countryterritoryCode'])

print(countries)

#class to work with data, makes data from one country out of the whole data set
class CountryData():
    def __init__(self, data_file, country):
        self.data_file = data_file
        self.country = country
        self.dataDict = []
        self.casesList = []
        self.deathsList = []
        self.plotMeanCases = False
        self.casesPerPeople = 100000
        self.setTimespan = True
        self.timespan = 90
        self.plotDeaths = False

        #get data for the right country out of the whole set
        for i in self.data_file:
            if i['countryterritoryCode'] == self.country:
                self.dataDict.append(i)

        #get the name of the country
        self.countryWhole = self.dataDict[0]['countriesAndTerritories']

        #define the length of the processed timespan
        if self.setTimespan:
            self.dataDict = self.dataDict[:self.timespan]

    #extract all case and death data to plot it later
    def extractCases(self):

        #gets list of cases to plot, reverse it to be in the right time order
        for i in self.dataDict:
            self.casesList.append(i['cases'])
        del self.casesList[-1]
        self.casesList.reverse()

        #get time steps for plot
        self.timesteps = np.arange(len(self.casesList))

        #whether to get the cases per xx people
        if self.plotMeanCases:
            for i in range(len(self.casesList)):
                self.casesList[i] = self.casesList[i] * (self.casesPerPeople/int(self.dataDict[0]['popData2020']))

        #exactely same procedure for deaths
        if self.plotDeaths:
            for i in self.dataDict:
                self.deathsList.append(i['deaths'])
            del self.deathsList[-1]
            self.deathsList.reverse()

            if self.plotMeanCases:
                for i in range(len(self.deathsList)):
                    self.deathsList[i] = self.deathsList[i] * (self.casesPerPeople / int(self.dataDict[0]['popData2020']))

    #shows cases and country dictionary
    def showData(self):
        print(self.casesList)
        a = []
        for i in self.data_file:
            if i['countryterritoryCode'] == self.country:
                a.append(i)
        print(a)

    #plots the graph of the country
    def plot(self):
        fig = plt.figure()
        fig.suptitle('Cases in %s' %self.countryWhole)
        ax = fig.add_subplot(111)
        ax.plot(self.timesteps,self.casesList, label='Cases')

        if self.plotDeaths:
            ax.plot(self.timesteps,self.deathsList,label='Deaths')

        ax.set_xlabel('Time (d)')
        ax.set_ylabel('Number of Cases')
        ax.grid(b=True, which='major', c='black', lw=1, ls='-', alpha=0.25)
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        plt.show()

#plot every country
#for i in countries:
 #   current_country = CountryData(EU_data_dict, i)
  #  current_country.extractCases()
   # current_country.plot()
    #if keyboard.is_pressed('q'):
#        break
 #   if keyboard.is_pressed('c'):
  #      continue

#random country output
#Rdm = CountryData(EU_data_dict, countries[random.randint(0,len(countries))])
#Rdm.extractCases()
#Rdm.plot()


c = CountryData(EU_data_dict, 'DEU')
c.extractCases()
c.plot()

#sample with Norway
#NOR = CountryData(EU_data_dict, 'NOR')
#NOR.extractCases()
#NOR.showData()
#NOR.plot()


