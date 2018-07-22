import math
import first_verify
import second_verify
from matplotlib import pyplot as plt

ip_list = ["192.168.62.116", "192.168.62.117", "192.168.62.119"]
ip_count = [0, 0, 0]

p_values = []

count = 0
file = open("alert-1", "r")
for line in file:
    new_list = line.split(' ')
    for i in range(0, 3):
        if new_list[9] == ip_list[i]:
            ip_count[i] += 1
    count += 1
    if count % 100 == 0:
        p_values.append(ip_count)
        ip_count = [0, 0, 0]
p_values.append(ip_count)

print(p_values)
exit()

# The upper code is shifted to another file #

p_values = [[0.2, 0.2, 0.2, 0.2, 0.2]]
q_values = [[0.2, 0.2, 0.2, 0.2, 0.2]]

# calculation for p , Renyi_s entropy of order alpha
alpha = 0
h_x_p = []
iteration = 5
elem_no = 5
for a in range(0, iteration):
    p_sum = 0
    for i in range(elem_no):
        p_sum += math.pow(p_values[0][i], alpha)
    h_x_p.append((1 / (1 - alpha)) * math.log(p_sum, 2))
    alpha += 0.50000000001
print(h_x_p)

# verification for p
first_verify.cal(p_values, elem_no)

# calculation for q
alpha = 0
h_x_q = []
for a in range(0, iteration):
    q_sum = 0
    for i in range(elem_no):
        q_sum += math.pow(q_values[0][i], alpha)
    h_x_q.append((1 / (1 - alpha)) * math.log(q_sum, 2))
    alpha += 0.50000000001
print(h_x_q)

# verification for q
first_verify.cal(q_values, elem_no)

# calculation for p||q
alpha = 0
h_x_pq = []
for a in range(0, iteration):
    pq_sum = 0
    for i in range(elem_no):
        pq_sum += (math.pow(p_values[0][i], alpha) * math.pow(q_values[0][i], (1 - alpha)))
    h_x_pq.append((-1 / (1 - alpha)) * math.log(pq_sum, 2))
    alpha += 0.50000000001
print(h_x_pq)

# verification for pq
second_verify.cal(p_values, q_values, elem_no)
