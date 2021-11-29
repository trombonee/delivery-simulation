# Meal Delivery Simulation
## Background
The goal of this group thesis project was to apply reinforcement learning to a stochastic control problem. The chosen area of application was using Q-Learning to optimize the scheduling of meal-delivery couriers (think Uber Eats, Skip the Dishes, etc) such that wait times are minimized. A lot of the focus was placed on working through the mathematics that underly such a problem. These simulation scripts were developed to help understand and visualize the behaviour of the system. 

## Simulation

The coolest files are [OrderSimulator](https://github.com/trombonee/delivery-simulation/blob/master/Simulation/OrderSimulator.py) and [Courier](https://github.com/trombonee/delivery-simulation/blob/master/Simulation/Courier.py) which implement the classes that are used to simulate the problem. 

When an OrderSimulator is initialized, a grid containing randomly placed houses, restaurants and couriers is created. The simulation works in timesteps (1 hour for example), where each house will place orders determined using a poisson clock. When a house places an order, it is randomly assigned to a restaurant (planning to add a distribution map to determine which restaurant the order is from). After orders are generated, they get assigned to a courier that will deliver them (this is where Q-Learning will be applied eventually).

Each Courier has a queue of orders that it is responsible for delivering. There are various methods implemented to make accessing data about each courier easier. To simulate the delivery of orders the perform_deliveries() method is called each timestep (probably the most interesting algorithm in this project).

