from __future__ import division
import math
from matplotlib import pyplot as plt


def cal(ip_list, ip_count, h_list):
    p_values = []
    q_values = []
    count = 0
    window_count = 0
    file = open("alert-1", "r")
    # read lines per window
    for line in file:
        new_list = line.split(' ')
        for i in range(0, len(ip_list)):
            if new_list[9] == ip_list[i]:
                ip_count[i] += 1
        count += 1
        # window stops here
        if count % 100 == 0:
            p_total = 0
            q_total = 0
            for i in range(0, len(ip_count)):
                if ip_count[i] < 40:
                    p_total += ip_count[i]
                else:
                    q_total += ip_count[i]
            p_values.append(p_total)
            q_values.append(q_total)

            window_count += 1
            # change length accordingly
            # ip_count = [0, 0, 0]
            ip_count = list(ip_count)
            for i in range(len(ip_count)):
                ip_count[i] = 0

    p_total = 0
    q_total = 0
    for i in range(0, len(ip_count)):
        if ip_count[i] < 40:
            p_total += ip_count[i]
        else:
            q_total += ip_count[i]
    p_values.append(p_total)
    q_values.append(q_total)

    p_h_list = []
    q_h_list = []
    for i in range(0, window_count):
        p_values[i] /= 100
        if p_values[i] == 0:
            p_h_list.append(0)
            continue
        total = p_values[i] * math.log(p_values[i], 2)
        total = -total
        p_h_list.append(total)
    for i in range(0, window_count):
        q_values[i] /= 100
        if q_values[i] == 0:
            q_h_list.append(0)
            continue
        print(q_values[i])
        total = q_values[i] * math.log(q_values[i], 2)
        total = -total
        q_h_list.append(total)

    plt.plot(p_h_list)
    plt.plot(q_h_list)
    plt.show()
