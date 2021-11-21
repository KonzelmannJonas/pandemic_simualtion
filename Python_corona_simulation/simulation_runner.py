from simulation import Simulation

sim = Simulation()
sim.Config.simulation_steps = 200
sim.Config.save_data = True
sim.run()