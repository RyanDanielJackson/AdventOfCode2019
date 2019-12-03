#####################################################
########## Advent of Code 2019 Day 01 ##############
#####################################################

import os
import math
total_fuel = 0
file = open('C:\\Users\\ryan.jackson\\Desktop\\input.txt', 'r')
for module in file.readlines():
    total_fuel += math.floor(int(module)/3) -2

print int(total_fuel)

