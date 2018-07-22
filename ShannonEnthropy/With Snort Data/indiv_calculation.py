from __future__ import division
import math
from matplotlib import pyplot as plt


def cal(ip_list, ip_count, h_list):
    pkt_count = []
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
            window_count += 1
            pkt_count.append(ip_count)
            # change length accordingly
            # ip_count = [0, 0, 0]
            ip_count = list(ip_count)
            for i in range(len(ip_count)):
                ip_count[i] = 0

    print(pkt_count)
    h_values = [[] for _ in range(len(ip_list))]

    for i in range(0, window_count):
        for j in range(0, len(ip_list)):
            pkt_count[i][j] /= 100
            total = pkt_count[i][j] * math.log(pkt_count[i][j], 2)
            total = -total
            h_values[j].append(total)

    for i in range(len(ip_list)):
        plt.plot(h_values[i])
    plt.show()
