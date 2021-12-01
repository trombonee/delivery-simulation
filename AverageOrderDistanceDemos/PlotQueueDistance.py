import os, sys
sys.path.append(os.getcwd())
from Simulation.OrderSimulator import Order_Simulator

import matplotlib.pyplot as plt

order_rate = [2, 3, 4, 5, 6, 7]

iters = 250

restaurants = [(2, 1), (3, 2)]
couriers = [(0, 0), (3, 3)]

for i in range(6):
    sim = Order_Simulator(4, 2, 2, order_rate[i])
    sim.grid_loader(restaurants, couriers)
    print('----------------------------------')
    print(f'Sim {i}:')
    sim.visualize_layout()
    ret_val = sim.average_order_distance(iters)

    x = range(iters)

    plt.plot(x, ret_val[0], label='Simple')
    plt.plot(x, ret_val[1], label='Nearest')
    plt.plot(x, ret_val[2], label='Shortest Queue')
    plt.title(f'Order Rate = {order_rate[i]}')
    plt.legend()
    plt.show()