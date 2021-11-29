import os, sys
sys.path.append(os.getcwd())
from Simulation.OrderSimulator import Order_Simulator

sim = Order_Simulator(4, 2, 2, 10)
print('----------------------------------------------------------------')
for i in range(10):
    print(f'Timestep: {i}')
    sim.simple_simulation(visualize=False, timestep=i)
    print('----------------------------------------------------------------')