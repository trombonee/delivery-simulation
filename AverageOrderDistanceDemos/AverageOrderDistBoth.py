from OrderSimulator import Order_Simulator

for i in range(5):
    sim = Order_Simulator(4, 2, 2, 10)
    print('----------------------------------')
    print(f'Sim {i}:')
    sim.visualize_layout()
    sim.average_order_distance(iters=100000)