from __future__ import division
import math
import calculation as c
import indiv_calculation as ic
import diff_calculation as dc

from matplotlib import pyplot as plt

# Alert file is alert-1
# change length accordingly
ip_list1 = ["192.168.62.116", "192.168.62.117", "192.168.62.119"]

ip_count1 = [None] * len(ip_list1)
for i in range(len(ip_list1)):
    ip_count1[i] = 0

h_list1 = []
#h_list1 = c.cal(ip_list1, ip_count1, h_list1)

#plt.plot(h_list1)
#plt.show()

# difference of entropy based on threshold
#dc.cal(ip_list1, ip_count1, h_list1)

# individual entropy graph
ic.cal(ip_list1, ip_count1, h_list1)
