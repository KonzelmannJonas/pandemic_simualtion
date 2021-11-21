import json
import numpy as np
import matplotlib.pyplot as plt

file_name = 'CoronavirusData/EU_coronavirus_data.json'

with open(file_name) as json_file:
    EU_data = json.load(json_file)["records"]

def getDate(dict):
    return dict['dateRep']

def getCases(dict):
    return dict['cases']

def getCountry(dict):
    return dict['countryterritoryCode']

def getCasesAtDayX(dict,country,day):
    cases = 0
    for i in dict:
        if getCountry(i)==country and getDate(i)==day:
            cases = getCases(i)
            break
    return cases

def getCountryDict(dict, country):
    country_dict = []
    for i in dict:
        if getCountry(i)==country:
            country_dict.append(i)
    return country_dict

def getMonthDict(dict, month):
    month_dict = []
    for i in dict:
        if i['month']==month:
            month_dict.append(i)
    return month_dict

def extractCasesFromDict(dict):
    cases_list = []
    for i in dict:
        cases_list.append(i['cases'])
    return cases_list

def getCasesForPlot(dict):
    plot_cases = []
    for i in dict:
        plot_cases.append(i['cases'])
    return plot_cases

def getDeathsForPlot(dict):
    plot_deaths = []
    for i in dict:
        plot_deaths.append(i['deaths'])
    return plot_deaths

AUT_cases = getCasesForPlot(getCountryDict(EU_data,'AUT'))
AUT_cases = AUT_cases[0:-1]
AUT_cases.reverse()

#AUT_deaths = getDeathsForPlot(getCountryDict(EU_data,'AUT'))
#AUT_deaths = AUT_deaths[0:-1]
#AUT_deaths.reverse()

#ddays = np.arange(len(AUT_deaths))
days = np.arange(len(AUT_cases))
"""
AUT_dict = getCountryDict(EU_data,'AUT')
AUT_06_dict =  getMonthDict(AUT_dict,'07')+ getMonthDict(AUT_dict,'06') +getMonthDict(AUT_dict,'05')
AUT_cases = extractCasesFromDict(AUT_06_dict)
#AUT_cases.reverse()
days = np.arange(len(AUT_cases))
"""
#print(AUT_cases)
plt.plot(days, AUT_cases)
#plt.plot(ddays,AUT_deaths,color='red')
plt.legend('Cases')
plt.show()



