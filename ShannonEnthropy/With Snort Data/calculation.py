from __future__ import division
import math
from matplotlib import pyplot as plt

def cal(ip_list, ip_count, h_list):
    p_values = []
    count = 0
    window_count = 0
    file = open("alert-1", "r")
    for line in file:
        new_list = line.split(' ')
        for i in range(0, len(ip_list)):
            if new_list[9] == ip_list[i]:
                ip_count[i] += 1
        count += 1
        if count % 100 == 0:
            window_count += 1
            p_values.append(ip_count)
            print(p_values)
            # change length accordingly
            # ip_count = [0, 0, 0]
            ip_count = list(ip_count)
            for i in range(len(ip_count)):
                ip_count[i] = 0

    p_values.append(ip_count)

    for i in range(0, window_count):
        total = 0
        for item in p_values[i]:
            item /= 100
            total += item * math.log(item, 2)
        total = -total
        h_list.append(total)
    return h_list
