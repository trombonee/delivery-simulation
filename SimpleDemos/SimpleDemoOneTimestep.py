import os, sys
sys.path.append(os.getcwd())
from Simulation.OrderSimulator import Order_Simulator

sim = Order_Simulator(4, 2, 2, 5)
sim.visualize_layout()
for i in range(2):
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    print(f'Timestep: {i}')
    sim.simple_simulation(visualize=True, timestep=i)