import os, sys
sys.path.append(os.getcwd())
from Simulation.OrderSimulator import Order_Simulator

for i in range(5):
    sim = Order_Simulator(4, 2, 2, 10)
    print('----------------------------------')
    print(f'Sim {i}:')
    sim.visualize_layout()
    sim.track_average_order_distance_simple(iters=100000)
