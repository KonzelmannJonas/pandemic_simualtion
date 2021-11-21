from load_coronadata_simdata_model_methods import PeopleToPlot
import numpy as np

scenario_num = int(input('*******\n'
                         '0 - Basic Data Graph\n'
                         '1 - Not working \n'
                         '2 - Not Working \n'
                         '3 - Cases Graph \n'
                         '4 - Deaths Graph \n'
                         '5 - Github Corona Example Graphs\n'
                         '6 - Example Interpolation\n'
                         '*********\n'
                         'What scenrio: '))

if scenario_num == 0:

    #########
    #Basic Data Graph
    #########

    # simulation folder
    sim_folder = 'Data/GithubSim/8'
    SIR_file = 'Data/SIR/SIR_data.npy'
    corona_file = 'Data/CoronaReal/index2_corona_data.npy'

    # get files
    SIR_array = np.load(SIR_file)
    simulation_population = np.load('%s/population.npy' % sim_folder)
    corona_data = np.load(corona_file)

    # number of time steps and interpolation translation interval
    time_steps = SIR_array[0]
    intpol_num = 40

    # define population data from SIR
    SIR_susceptible = SIR_array[1]
    SIR_infected = SIR_array[2]
    SIR_fatalities = SIR_array[4]
    SIR_recovered = SIR_array[3]

    SIR_data = [SIR_infected, SIR_fatalities]

    # get population data from Simulation
    simulation_infected = np.load('%s/infected.npy' % sim_folder)
    simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
    simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
    # suscptible doesnt work if time_steps has other format than simulation data
    # simulation_susceptible = np.full(len(time_steps),
    # len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered


    simulation_data = [simulation_infected, simulation_fatalities]


    graphNames = [['SIR Infizierte', 'SIR Todesfälle'], ['Corona Infizierte', 'Corona Todesfälle'],
                  ['Simulation Infizierte', 'Simulation Todesfälle']]  # ,['Corona Infected','Corona Fatalities'] for corona
    colors = [['blue', 'black'], ['green', 'yellow'], ['red', 'purple']]  # ,['green','red'] for real corona
    intpol_nums = [0, 0, 40]
    background_graphs = [False, False, False]
    pop_indexes = [0, 0, 0]

    data = [time_steps, SIR_data, corona_data, simulation_data]

    plotAllData = PeopleToPlot(data)

    plotAllData.graphNames = graphNames
    plotAllData.graphColor = colors
    plotAllData.interpolation_nums = intpol_nums
    plotAllData.backgroundGraph = background_graphs
    plotAllData.pop_indexes = pop_indexes

    plotAllData.interpolate_array()
    plotAllData.cutGraphs(3)
    # plotAllData.showData()

    plotAllData.plot()


elif scenario_num == 1:
    # simulation folder
    sim_folder = 'Data/GithubSim/8'
    SIR_file = 'Data/SIR/index0_SIR_data.npy'
    corona_file = 'Data/CoronaReal/index0_bag_corona_data_16082021.npy'

    # get files
    SIR_array = np.load(SIR_file)
    simulation_population = np.load('%s/population.npy' % sim_folder)
    corona_data = np.load(corona_file)

    # number of time steps and interpolation translation interval
    time_steps = SIR_array[0]
    intpol_num = 40

    # define population data from SIR
    SIR_susceptible = SIR_array[1]
    SIR_infected = SIR_array[2]
    SIR_fatalities = SIR_array[4]
    SIR_recovered = SIR_array[3]

    SIR_data = [SIR_infected, SIR_fatalities]

    # get population data from Simulation
    simulation_infected = np.load('%s/infected.npy' % sim_folder)
    simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
    simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
    # suscptible doesnt work if time_steps has other format than simulation data
    # simulation_susceptible = np.full(len(time_steps),
    # len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered

    simulation_data = [simulation_infected, simulation_fatalities]


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
graphNames = [[ 'Sim Infected', 'Sim Fatalities'],['SIR Infected', 'SIR Fatalities']] #,['Corona Infected','Corona Fatalities'] for corona
colors = [['blue', 'black'],['blue','black']] #,['green','red'] for real corona
intpol_nums = [40,0]
background_graphs = [False, True]

data = [time_steps, simulation_data, SIR_data]

plotAllData = PeopleToPlot(data)

plotAllData.graphNames = graphNames
plotAllData.graphColor = colors
plotAllData.interpolation_nums = intpol_nums
plotAllData.backgroundGraph = background_graphs

plotAllData.interpolate_array()
#plotAllData.showData()

plotAllData.plot()
"""

if scenario_num == 2:
    # simulation folder
    sim_folder = 'Data/GithubSim/8'
    SIR_file = 'Data/SIR/SIR_data.npy'
    corona_file = 'Data/CoronaReal/index0_bag_corona_data_16082021.npy'

    # get files
    SIR_array = np.load(SIR_file)
    simulation_population = np.load('%s/population.npy' % sim_folder)
    corona_data = np.load(corona_file)
    corona_data = corona_data[0]

    # number of time steps and interpolation translation interval
    time_steps = SIR_array[0]

    # define population data from SIR
    SIR_susceptible = SIR_array[1]
    SIR_infected = SIR_array[2]
    SIR_fatalities = SIR_array[4]
    SIR_recovered = SIR_array[3]

    SIR_data = [SIR_fatalities]

    # get population data from Simulation
    simulation_infected = np.load('%s/infected.npy' % sim_folder)
    simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
    simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
    # suscptible doesnt work if time_steps has other format than simulation data
    # simulation_susceptible = np.full(len(time_steps),
    # len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered


    simulation_data = [simulation_fatalities]


    graphNames = [[ 'SIR Fatalities'], [ 'Corona Fatalities'],
                  [ 'Sim fatalities']]  # ,['Corona Infected','Corona Fatalities'] for corona
    colors = [['black'], [ 'yellow'], [ 'purple']]  # ,['green','red'] for real corona
    intpol_nums = [0, 0, 40]
    background_graphs = [False, False, False]
    pop_indexes = [0, 0, 0]

    data = [time_steps, SIR_data, corona_data, simulation_data]

    plotAllData = PeopleToPlot(data)

    plotAllData.graphNames = graphNames
    plotAllData.graphColor = colors
    plotAllData.interpolation_nums = intpol_nums
    plotAllData.backgroundGraph = background_graphs
    plotAllData.pop_indexes = pop_indexes

    plotAllData.interpolate_array()
    plotAllData.cutGraphs(3)
    # plotAllData.showData()

    plotAllData.plot()


# simulation folder
sim_folder = 'Data/GithubSim/2_githubsim_folder/14'
SIR_file = 'Data/SIR/3_SIR_folder/3_SIR_data.npy'
corona_file = 'Data/CoronaReal/index2_corona_data.npy'


if scenario_num == 3:

    #######
    #Only Cases graphed
    #######



    # get files
    SIR_array = np.load(SIR_file)
    simulation_population = np.load('%s/population.npy' % sim_folder)
    corona_data = np.load(corona_file)


    # number of time steps and interpolation translation interval
    time_steps = SIR_array[0]
    intpol_num = 40

    # define population data from SIR
    SIR_susceptible = SIR_array[1]
    SIR_infected = SIR_array[2]
    SIR_fatalities = SIR_array[4]
    SIR_recovered = SIR_array[3]

    SIR_data = [SIR_infected]

    # get population data from Simulation
    simulation_infected = np.load('%s/infected.npy' % sim_folder)
    simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
    simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
    # suscptible doesnt work if time_steps has other format than simulation data
    # simulation_susceptible = np.full(len(time_steps),
    # len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered


    simulation_data = [simulation_infected]


    graphNames = [['SIR Infizierte'], ['Corona Infizierte'],
                  ['Simulation Infizierte']]  # ,['Corona Infected','Corona Fatalities'] for corona
    colors = [['blue'], ['green'], ['red']]  # ,['green','red'] for real corona
    intpol_nums = [0, 0, 37]
    background_graphs = [False, False, False]
    pop_indexes = [0, 0, 0]

    data = [time_steps, [SIR_data[0]], [corona_data[0]], [simulation_data[0]]]

    plotAllData = PeopleToPlot(data)
    plotAllData.graphNames = graphNames
    plotAllData.graphColor = colors
    plotAllData.interpolation_nums = intpol_nums
    plotAllData.backgroundGraph = background_graphs
    plotAllData.pop_indexes = pop_indexes

    plotAllData.interpolate_array()
    plotAllData.cutGraphs(3)
    # plotAllData.showData()

    plotAllData.plot()

    print(len(time_steps))

if scenario_num == 4:

    #########
    #Only Deaths graphed
    #########



    # get files
    SIR_array = np.load(SIR_file)
    simulation_population = np.load('%s/population.npy' % sim_folder)
    corona_data = np.load(corona_file)

    # number of time steps and interpolation translation interval
    time_steps = SIR_array[0]
    intpol_num = 40

    # define population data from SIR
    SIR_susceptible = SIR_array[1]
    SIR_infected = SIR_array[2]
    SIR_fatalities = SIR_array[4]
    SIR_recovered = SIR_array[3]

    SIR_data = [SIR_infected, SIR_fatalities]

    # get population data from Simulation
    simulation_infected = np.load('%s/infected.npy' % sim_folder)
    simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
    simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
    # suscptible doesnt work if time_steps has other format than simulation data
    # simulation_susceptible = np.full(len(time_steps),
    # len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered


    simulation_data = [simulation_infected, simulation_fatalities]


    graphNames = [['SIR Todesfälle'], ['Corona Todesfälle'],
                  ['Simulation Todesfälle']]  # ,['Corona Infected','Corona Fatalities'] for corona
    colors = [['black'], ['green'], [ 'purple']]  # ,['green','red'] for real corona
    intpol_nums = [0, 0, 37]
    background_graphs = [False, False, False]
    pop_indexes = [0, 0, 0]

    data = [time_steps, [SIR_data[1]], [corona_data[1]], [simulation_data[1]]]

    plotAllData = PeopleToPlot(data)

    plotAllData.graphNames = graphNames
    plotAllData.graphColor = colors
    plotAllData.interpolation_nums = intpol_nums
    plotAllData.backgroundGraph = background_graphs
    plotAllData.pop_indexes = pop_indexes

    plotAllData.interpolate_array()
    plotAllData.cutGraphs(3)
    # plotAllData.showData()

    plotAllData.plot()

    print(len(time_steps))

if scenario_num == 5:
    #########
    # Basic Data Graph for Github Corona Simulation
    #########

    # simulation folder
    sim_folder = 'Data/GithubSim/Examples_arbeit/Example3/21'
    SIR_file = 'Data/SIR/SIR_data.npy'

    # get files
    simulation_population = np.load('%s/population.npy' % sim_folder)
    SIR_array = np.load(SIR_file)

    # number of time steps and interpolation translation interval
    time_steps = SIR_array[0]

    # get population data from Simulation
    simulation_infected = np.load('%s/infected.npy' % sim_folder)
    simulation_recovered = np.load('%s/recovered.npy' % sim_folder)
    simulation_fatalities = np.load('%s/fatalities.npy' % sim_folder)
    # suscptible doesnt work if time_steps has other format than simulation data
    simulation_susceptible = np.full(len(time_steps),len(simulation_population)) - simulation_infected - simulation_fatalities - simulation_recovered

    simulation_data = [simulation_susceptible, simulation_infected, simulation_fatalities, simulation_recovered]

    graphNames = [ ['Anfällige', 'Infizierte', 'Todesfälle', 'Genesen']]  # ,['Corona Infected','Corona Fatalities'] for corona
    colors = [['purple','red', 'black','green']]  # ,['green','red'] for real corona
    intpol_nums = [0]
    background_graphs = [False]
    pop_indexes = [0]

    data = [time_steps, simulation_data]

    plotAllData = PeopleToPlot(data)

    plotAllData.graphNames = graphNames
    plotAllData.graphColor = colors
    plotAllData.interpolation_nums = intpol_nums
    plotAllData.backgroundGraph = background_graphs
    plotAllData.pop_indexes = pop_indexes

    #plotAllData.interpolate_array()
    #plotAllData.cutGraphs(3)
    # plotAllData.showData()

    plotAllData.plot()

if scenario_num == 6:

    SIR_file_1 = 'Data/SIR/3_SIR_folder/3_SIR_data.npy'
    SIR_file_2 = 'Data/SIR/2_SIR_folder/2_SIR_data.npy'
    # get files
    SIR_array_1 = np.load(SIR_file_1)
    SIR_array_2 = np.load(SIR_file_2)


    # number of time steps and interpolation translation interval
    time_steps = SIR_array_1[0]


    # define population data from SIR
 #   SIR_susceptible = SIR_array[1]
 #   SIR_infected = SIR_array[2]
 #   SIR_fatalities = SIR_array[4]
#    SIR_recovered = SIR_array[3]


    SIR_data_1 = [SIR_array_1[2]]
    SIR_data_2 = [SIR_array_2[2]]

    graphNames = [['Beispielgraph #1'], ['Beispielgraph #2']]  # ,['Corona Infected','Corona Fatalities'] for corona
    colors = [['blue'],['red']]  # ,['green','red'] for real corona
    intpol_nums = [12, 10]
    background_graphs = [False, False]
    pop_indexes = [0, 0]

    data = [time_steps, SIR_data_1, SIR_data_2]

    plotAllData = PeopleToPlot(data)

    plotAllData.graphNames = graphNames
    plotAllData.graphColor = colors
    plotAllData.interpolation_nums = intpol_nums
    plotAllData.backgroundGraph = background_graphs
    plotAllData.pop_indexes = pop_indexes

    plotAllData.interpolate_array()
  #  plotAllData.cutGraphs(3)
    # plotAllData.showData()

    plotAllData.plot()
