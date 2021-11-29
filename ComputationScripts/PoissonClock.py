import numpy as np

last_step = 24   # to simulate one day, with 1hr intervals
rate = 245.0 / last_step  # number of orders per day

for time_step in range(1, last_step + 1)
    number_of_new_orders = numpy.random.poisson(rate)
    print(number_of_new_orders)
    for new_order_number in range(number_of_new_orders):
    
        ##Assign a house and restaurant associated with the order 
