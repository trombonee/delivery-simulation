import os, sys
sys.path.append(os.getcwd())
from Simulation.OrderSimulator import Order_Simulator

sim = Order_Simulator(4, 2, 2, 5)
print('----------------------------------------------------------------')
sim.visualize_layout()
for i in range(3):
    print(f'Timestep: {i}')
    sim.nearest_simulation(visualize=True, timestep=i)
    print('----------------------------------------------------------------')