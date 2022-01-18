import random
import numpy as np
import os, sys
sys.path.append(os.getcwd())
from Simulation.Courier import Courier
import copy

class Order_Simulator():

    def __init__(self, grid_length, num_restaurants, num_couriers, order_rate):
        '''
        Initialize function will save information about current state space layout
        and create the restaurants, houses and couriers
        '''
        self.grid_length = grid_length
        self.num_restaurants = num_restaurants
        self.num_couriers = num_couriers
        self.order_rate = order_rate
        self.initialize_restaurants_and_houses()
        self.initialize_couriers()
    
    def grid_loader(self, restaurants, couriers):
        '''
        This function can be used to load in a custom state space (for testing purposes)
        Restaurants: An array of coordinates where restuarants should be
        Couriers: An array of cooridinates where couriers should be
        '''
        self.restaurants = {}
        for i,r in enumerate(restaurants):
            self.restaurants[i] = r
        
        self.num_restaurants = len(self.restaurants)
        
        self.couriers = {}
        for i, c in enumerate(couriers):
            self.couriers[i] = Courier(self, 15)
            self.couriers[i].location = c
        
        self.num_couriers = len(self.couriers)
        
        all_locations = []
        for i in range(self.grid_length):
            for j in range(self.grid_length):
                all_locations.append((i, j))

        self.houses = {}
        count = 0
        for loc in all_locations:
            if loc in self.restaurants.values():
                continue      
            self.houses[count] = loc
            count += 1

    def initialize_restaurants_and_houses(self):
        '''
        Initializes positions of restaurants and houses within grid
        '''
        self.restaurants = {} 
        for i in range(self.num_restaurants):
            restaurant_location = (random.randint(0, self.grid_length - 1), random.randint(0, self.grid_length - 1))
            while restaurant_location in self.restaurants.values(): 
                restaurant_location = (random.randint(0, self.grid_length - 1), random.randint(0, self.grid_length - 1)) 
            self.restaurants[i] = restaurant_location
        
        all_locations = []
        for i in range(self.grid_length):
            for j in range(self.grid_length):
                all_locations.append((i, j))

        self.houses = {}
        count = 0
        for loc in all_locations:
            if loc in self.restaurants.values():
                continue      
            self.houses[count] = loc
            count += 1
    
    def initialize_couriers(self):
        '''
        Initialize courier objects 
        '''
        self.couriers = {}
        for i in range(self.num_couriers):
            self.couriers[i] = Courier(self, 15)

    def generate_orders_for_timestep(self):
        '''
        Generates random orders using possion clock for each house. 
        Randomly chooses restaurant to order from
        '''
        orders = []
        for house in self.houses:
            num_house_orders = np.random.poisson(
                self.order_rate / (self.grid_length ** 2 - self.num_restaurants))
            for i in range(num_house_orders):
                orders.append((random.randint(0, self.num_restaurants - 1), house))

        return orders
    
    def visualize_layout(self): 
        '''
        Prints out layout of houses/restaurants for visualization purposes
        '''
        arr = [[None] * self.grid_length for i in range(self.grid_length)]

        for restaurant in self.restaurants.values(): arr[restaurant[1]][restaurant[0]] = 'R'
      
        for house in self.houses.values(): arr[house[1]][house[0]] = 'H'

        for courier_num, courier in self.couriers.items():
            x, y = courier.location
            arr[y][x] += 'C' + str(courier_num)
            
        for row in arr: print(row)
    
    '''
    Below are all the custom simulations that can be run
    They are very similar but differ in how they assign orders
    (greedy, random, etc)
    '''
    
    def simple_simulation(self, visualize=False, timestep=None):
        '''
        Simulation where orders are assigned randomly to either courier
        '''
        orders = self.generate_orders_for_timestep()
        print(f'There were {len(orders)} orders placed this timestep:')
        for i, order in enumerate(orders):
            restaurant, house = self.restaurants[order[0]], self.houses[order[1]]
            courier_num = random.randint(0, self.num_couriers - 1)
            if visualize:
                print(f'Order {restaurant} -> {house} assigned to courier {courier_num}')
            courier = self.couriers[courier_num]
            courier.add_order(restaurant, house)
        
        for i, courier in self.couriers.items():
            if visualize:
                print('---------------------------------------')
            print(f'Courier {i}:')
            courier.perform_deliveries(visualize=visualize, timestep=timestep)
    
    def nearest_simulation(self, visualize=False, timestep=None):
        '''
        Simulation where orders are assigned randomly to either courier
        '''
        orders = self.generate_orders_for_timestep()
        print(f'There were {len(orders)} orders placed this timestep:')
        for i, order in enumerate(orders):
            restaurant, house = self.restaurants[order[0]], self.houses[order[1]]
            courier_num = min(self.couriers.items(), key=lambda x:x[1].order_dist_from_last_queue(restaurant, restaurant))[0]
            if visualize:
                print(f'Order {restaurant} -> {house} assigned to courier {courier_num}')
            courier = self.couriers[courier_num]
            courier.add_order(restaurant, house)
        
        for i, courier in self.couriers.items():
            if visualize:
                print('---------------------------------------')
            print(f'Courier {i}:')
            courier.perform_deliveries(visualize=visualize, timestep=timestep)
    
    def shortest_queue_simulation(self, visualize=False, timestep=None):
        orders = self.generate_orders_for_timestep()
        print(f'There were {len(orders)} orders placed this timestep:')
        for i, order in enumerate(orders):
            restaurant, house = self.restaurants[order[0]], self.houses[order[1]]
            courier_num = min(self.couriers.items(), key=lambda x: x[1].get_queue_length())[0]
            if visualize:
                print(f'Order {restaurant} -> {house} assigned to courier {courier_num}')
            courier = self.couriers[courier_num]
            courier.add_order(restaurant, house)
        
        for i, courier in self.couriers.items():
            if visualize:
                print('---------------------------------------')
            print(f'Courier {i}:')
            courier.perform_deliveries(visualize=visualize, timestep=timestep)
    
    def track_average_order_distance_nearest(self, iters=1000):
        order_count = [0, 0]
        dist = [0, 0]
        for j in range(iters):
            orders = self.generate_orders_for_timestep()
            for i, order in enumerate(orders):
                restaurant, house = self.restaurants[order[0]], self.houses[order[1]]
                courier_num = min(self.couriers.items(
                ), key=lambda x: x[1].order_dist_from_last_queue(restaurant, restaurant))[0]
                courier = self.couriers[courier_num]
                order_count[courier_num] += 1
                dist[courier_num] += courier.order_dist_from_last_queue(restaurant, house)
                courier.add_order(restaurant, house)
                
            for i, courier in self.couriers.items():
                courier.perform_deliveries(visualize=None)
        
        for i, courier in self.couriers.items():
            print(f'Courier {i} average order distance: {round(dist[i]/order_count[i], 3)}')
    
    def track_average_order_distance_simple(self, iters=1000):
        order_count = [0, 0]
        dist = [0, 0]
        for j in range(iters):
            orders = self.generate_orders_for_timestep()
            for i, order in enumerate(orders):
                restaurant, house = self.restaurants[order[0]
                                                     ], self.houses[order[1]]
                courier_num = random.randint(0, self.num_couriers - 1)
                courier = self.couriers[courier_num]
                order_count[courier_num] += 1
                dist[courier_num] += courier.order_dist_from_last_queue(
                    restaurant, house)
                courier.add_order(restaurant, house)

            for i, courier in self.couriers.items():
                courier.perform_deliveries(visualize=None)

        for i, courier in self.couriers.items():
            print(
                f'Courier {i} average order distance: {round(dist[i]/order_count[i], 3)}')
    
    def track_average_order_distance_shortest(self, iters=1000):
        order_count = [0, 0]
        dist = [0, 0]
        for j in range(iters):
            orders = self.generate_orders_for_timestep()
            for i, order in enumerate(orders):
                restaurant, house = self.restaurants[order[0]
                                                     ], self.houses[order[1]]
                courier_num = min(self.couriers.items(
                ), key=lambda x: x[1].get_queue_length())[0]
                courier = self.couriers[courier_num]
                order_count[courier_num] += 1
                dist[courier_num] += courier.order_dist_from_last_queue(
                    restaurant, house)
                courier.add_order(restaurant, house)

            for i, courier in self.couriers.items():
                courier.perform_deliveries(visualize=None)

        for i, courier in self.couriers.items():
            print(
                f'Courier {i} average order distance: {round(dist[i]/order_count[i], 3)}')

    def average_order_distance(self, iters=1000):
        order_count1 = [0] * self.num_couriers
        dist1 = [0] * self.num_couriers
        order_count2 = [0] * self.num_couriers
        dist2 = [0] * self.num_couriers
        order_count3 = [0] * self.num_couriers
        dist3 = [0] * self.num_couriers
        couriers_1 = copy.deepcopy(self.couriers)
        couriers_2 = copy.deepcopy(self.couriers)
        couriers_3 = copy.deepcopy(self.couriers)
        track_simple = []
        track_nearest = []
        track_shortest = []

        for j in range(iters):
            orders = self.generate_orders_for_timestep()
            for i, order in enumerate(orders):
                restaurant, house = self.restaurants[order[0]
                                                     ], self.houses[order[1]]
                courier_num1 = random.randint(0, self.num_couriers - 1)
                courier_num2 = min(couriers_2.items(
                ), key=lambda x: x[1].order_dist_from_last_queue(restaurant, restaurant))[0]
                courier_num3 = min(couriers_3.items(
                ), key=lambda x: x[1].get_queue_length())[0]
                courier_1 = couriers_1[courier_num1]
                courier_2 = couriers_2[courier_num2]
                courier_3 = couriers_3[courier_num3]
                order_count1[courier_num1] += 1
                dist1[courier_num1] += courier_1.order_dist_from_last_queue(
                    restaurant, house)
                order_count2[courier_num2] += 1
                dist2[courier_num2] += courier_2.order_dist_from_last_queue(
                    restaurant, house)
                order_count3[courier_num3] += 1
                dist3[courier_num3] += courier_3.order_dist_from_last_queue(
                    restaurant, house)
                courier_1.add_order(restaurant, house)
                courier_2.add_order(restaurant, house)
                courier_3.add_order(restaurant, house)

            sum1, sum2, sum3 = 0, 0, 0 
            for courier1, courier2, courier3 in zip(couriers_1.values(), couriers_2.values(), couriers_3.values()):
                courier1.perform_deliveries(visualize=None)
                courier2.perform_deliveries(visualize=None)
                courier3.perform_deliveries(visualize=None)
                sum1 += courier1.queue_distance
                sum2 += courier2.queue_distance
                sum3 += courier3.queue_distance
            
            track_simple.append(sum1)
            track_nearest.append(sum2)
            track_shortest.append(sum3)

        dist_tot1, dist_tot2, dist_tot3 = 0, 0, 0
        num1, num2, num3 = 0, 0, 0
        for i in couriers_1:
            dist_tot1 += dist1[i]
            dist_tot2 += dist2[i]
            dist_tot3 += dist3[i]
            num1 += order_count1[i]
            num2 += order_count2[i]
            num3 += order_count3[i]
            print(
                f'Courier {i} average order distance (Simple): {dist1[i]/order_count1[i]}')
            if order_count2[i] > 0:
                print(
                f'Courier {i} average order distance (Greedy): {dist2[i]/order_count2[i]}')
            print(
                f'Courier {i} average order distance (Shortest Queue): {dist3[i]/order_count3[i]}')
        print(f'Overall average (Simple): {dist_tot1 / num1}')
        print(f'Overall average (Greedy): {dist_tot2 / num2}')
        print(f'Overall average (Shortest Queue): {dist_tot3 / num3}')

        return track_simple, track_nearest, track_shortest

    
