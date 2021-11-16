import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 2000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0, D0 = 1, 0, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 - D0
initNums=[I0,R0,D0]
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days), death rate delta
beta, gamma, delta = 0.4, 1./22, 0.001
rates=[beta,gamma,delta]
# A grid of time points (in days)
num_of_days = 200
t = np.linspace(0, num_of_days, num_of_days)


# The SIR model differential equations.
def deriv(y, t, N, beta, gamma, delta):
    S, I, R, D = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I - delta * I
    dRdt = gamma * I
    dDdt = delta * I
    return dSdt, dIdt, dRdt, dDdt

class SIR_simulation():
    def __init__(self, pop_size, initialNumsDepartment, rates, num_of_days):
        self.pop_size = pop_size   #total population
        self.save_file_name = 'SIR_data.npy'
        # Initial number of infected and recovered individuals, I0 and R0.
        self.I0 = initialNumsDepartment[0]
        self.R0 = initialNumsDepartment[1]
        self.D0 = initialNumsDepartment[2]
        self.S0 = self.pop_size - self.I0 -self.R0-self.D0 # Everyone else, S0, is susceptible to infection initially.

        self.y0 = self.S0, self.I0,self.R0,self.D0

        #Values of sim
        self.S = 0
        self.I = 0
        self.R = 0
        self.D = 0

        # Contact rate, beta, and mean recovery rate, gamma, (in 1/days), death rate delta
        self.beta = rates[0]
        self.gamma = rates[1]
        self.delta = rates[2]

        #time grid
        self.t = np.linspace(0, num_of_days, num_of_days)
        self.num_of_days = num_of_days


    def getValues(self):
            # Initial conditions vector
        self.y0 = self.S0, self.I0, self.R0, self.D0
        # Integrate the SIR equations over the time grid, t.
        ret = odeint(deriv, self.y0, self.t, args=(self.pop_size, self.beta, self.gamma, self.delta))
        self.S, self.I, self.R, self.D = ret.T

    def plot(self):
        # Plot the data on three separate curves for S(t), I(t) and R(t)
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, facecolor='w', axisbelow=True)
        ax.plot(self.t, self.S, 'b', alpha=0.5, lw=2, label='Anfällige')
        ax.plot(self.t, self.I, 'r', alpha=0.5, lw=2, label='Infizierte')
        ax.plot(self.t, self.R, 'g', alpha=0.5, lw=2, label='Genesen')
        ax.plot(self.t, self.D, 'purple', alpha=0.5, lw=2, label='Todesfälle')
        ax.set_xlabel('Zeit [d]')
        ax.set_ylabel('Anzahl Fälle')
        # ax.set_ylim(0,1.2)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='black', lw=2, ls='-', alpha=0.25)
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        # for spine in ('top', 'right', 'bottom', 'left'):
        #    ax.spines[spine].set_visible(False)
        plt.show()

    def safeData(self):
        data = np.zeros((5, self.num_of_days))

        data[0] = self.t
        data[1] = self.S
        data[2] = self.I
        data[3] = self.R
        data[4] = self.D

        np.save(self.save_file_name, data)

        for i in range(1, 5):
            print(data[i][-1])

    def save_parameters(self):
        with open('parameters_SIR.txt', 'w') as para_file:
            para_file.write('Population: %i\n'%self.pop_size)
            para_file.write('Contact Rate (Beta): %f\n'%self.beta)
            para_file.write('Recovery Rate (Gamma): %f\n'%self.gamma)
            para_file.write('Death Rate (Delta): %f\n'%self.delta)
            para_file.close()

    def getHighest(self, list):
        biggest_num = 0
        for i in list:
            if i > biggest_num:
                biggest_num = i
        return biggest_num

"""
data = np.zeros((5,num_of_days))

data[0] = t
data[1] = S
data[2] = I
data[3] = R
data[4] = D

np.save('SIR_data.npy', data)

for i in range(1,5):
    print(data[i][-1])
"""


