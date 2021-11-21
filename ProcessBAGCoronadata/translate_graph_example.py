import numpy as np
import matplotlib.pyplot as plt

num_of_steps = 150
steps = np.arange(num_of_steps)

f1 = np.sin(steps)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(steps,f1)
plt.show()