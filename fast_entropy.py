from __future__ import division
import math

my_list1 = [2605, 1831, 1786, 1743, 1023, 295, 204]
x_it = my_list1[0]
my_list2 = [2367, 1956, 1890, 1865, 299, 495, 377]
x_it_next = my_list2[0]

s = 0
for i in my_list1:
    s += i

p = - math.log(x_it / s, 2)
print(p)
T = - math.log(x_it_next / x_it, 2)
print(T)
H = p + T
print(H)
