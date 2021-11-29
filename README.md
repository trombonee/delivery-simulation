# Meal Delivery Simulation
## Background
The goal of this group thesis project was to apply reinforcement learning to a stochastic control problem. The chosen area of application was using Q-Learning to optimize the scheduling of meal-delivery couriers (think Uber Eats, Skip the Dishes, etc) such that wait times are minimized. A lot of the focus was placed on working through the mathematics that underly such a problem. These simulation scripts were developed to help understand and visualize the behaviour of the system. 

## Simulation

The coolest files are [OrderSimulator](https://github.com/trombonee/delivery-simulation/blob/master/Simulation/OrderSimulator.py) and [Courier](https://github.com/trombonee/delivery-simulation/blob/master/Simulation/Courier.py) which implement the classes that are used to simulate the problem. 

When an OrderSimulator is initialized, a grid containing randomly placed houses, restaurants and couriers is created. The simulation works in timesteps (1 hour for example), where each house will place orders determined using a poisson clock. When a house places an order, it is randomly assigned to a restaurant (planning to add a distribution map to determine which restaurant the order is from). After orders are generated, they get assigned to a courier that will deliver them (this is where Q-Learning will be applied eventually).

Each Courier has a queue of orders that it is responsible for delivering. There are various methods implemented to make accessing data about each courier easier. To simulate the delivery of orders the perform_deliveries() method is called each timestep (probably the most interesting algorithm in this project).

Some sample output can be seen below. Planning on making the visualizations better (maybe with manim) in the near future:

```
----------------------------------------------------------------
['H', 'H', 'H', 'H']
['H', 'HC1', 'H', 'HC0']
['H', 'H', 'R', 'R']
['H', 'H', 'H', 'H']
Timestep: 0
There were 6 orders placed this timestep:
Order (3, 2) -> (0, 1) assigned to courier 0
Order (2, 2) -> (0, 1) assigned to courier 1
Order (3, 2) -> (0, 2) assigned to courier 0
Order (3, 2) -> (1, 3) assigned to courier 1
Order (2, 2) -> (3, 0) assigned to courier 0
Order (2, 2) -> (3, 3) assigned to courier 1
---------------------------------------
Courier 0:
Start:
L_0 = 17, A_0 = 17, S_0 = 15, Queue Length: 3
Completed order - Started: (3, 1) to Restaurant: (3, 2) to House: (0, 1)
Distance covered: 5
['H', 'H', 'H', 'H']
['HC0', 'HC1', 'H', 'H']
['H', 'H', 'R', 'R']
['H', 'H', 'H', 'H']
---------------------------------------------------------------------
Completed order - Started: (0, 1) to Restaurant: (3, 2) to House: (0, 2)
Distance covered: 7
['H', 'H', 'H', 'H']
['H', 'HC1', 'H', 'H']
['HC0', 'H', 'R', 'R']
['H', 'H', 'H', 'H']
---------------------------------------------------------------------
Partially completed order - Starting: (0, 2) to Restaurant: (2, 2) to House: (3, 0)
Made it to: (3, 2), distance covered: 3
['H', 'H', 'H', 'H']
['H', 'HC1', 'H', 'H']
['H', 'H', 'R', 'RC0']
['H', 'H', 'H', 'H']
-------------------------------------------------------------
End:
L_0 = 2, A_0 = 0, S_0 = 15, Queue Length: 1
---------------------------------------
Courier 1:
Start:
L_0 = 16, A_0 = 16, S_0 = 15, Queue Length: 3
Completed order - Started: (1, 1) to Restaurant: (2, 2) to House: (0, 1)
Distance covered: 5
['H', 'H', 'H', 'H']
['HC1', 'H', 'H', 'H']
['H', 'H', 'R', 'RC0']
['H', 'H', 'H', 'H']
---------------------------------------------------------------------
Completed order - Started: (0, 1) to Restaurant: (3, 2) to House: (1, 3)
Distance covered: 7
['H', 'H', 'H', 'H']
['H', 'H', 'H', 'H']
['H', 'H', 'R', 'RC0']
['H', 'HC1', 'H', 'H']
---------------------------------------------------------------------
Partially completed order - Starting: (1, 3) to Restaurant: (2, 2) to House: (3, 3)
Made it to: (3, 2), distance covered: 3
['H', 'H', 'H', 'H']
['H', 'H', 'H', 'H']
['H', 'H', 'R', 'RC0C1']
['H', 'H', 'H', 'H']
-------------------------------------------------------------
End:
L_0 = 1, A_0 = 0, S_0 = 15, Queue Length: 1
----------------------------------------------------------------
Timestep: 1
There were 3 orders placed this timestep:
Order (2, 2) -> (0, 0) assigned to courier 0
Order (3, 2) -> (2, 0) assigned to courier 1
Order (3, 2) -> (2, 1) assigned to courier 0
---------------------------------------
Courier 0:
Start:
L_1 = 16, A_1 = 14, S_1 = 15, Queue Length: 3
Completed order - Started: (3, 2) to Restaurant: (3, 0) to House: (3, 0)
Distance covered: 2
['H', 'H', 'H', 'HC0']
['H', 'H', 'H', 'H']
['H', 'H', 'R', 'RC1']
['H', 'H', 'H', 'H']
---------------------------------------------------------------------
Completed order - Started: (3, 0) to Restaurant: (2, 2) to House: (0, 0)
Distance covered: 7
['HC0', 'H', 'H', 'H']
['H', 'H', 'H', 'H']
['H', 'H', 'R', 'RC1']
['H', 'H', 'H', 'H']
---------------------------------------------------------------------
Partially completed order - Starting: (0, 0) to Restaurant: (3, 2) to House: (2, 1)
Made it to: (2, 2), distance covered: 6
['H', 'H', 'H', 'H']
['H', 'H', 'H', 'H']
['H', 'H', 'RC0', 'RC1']
['H', 'H', 'H', 'H']
-------------------------------------------------------------
End:
L_1 = 1, A_1 = 0, S_1 = 15, Queue Length: 1
---------------------------------------
```
