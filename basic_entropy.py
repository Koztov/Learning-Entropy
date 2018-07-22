# Entropy based on two occurrences of an event
# Occurrences of head and tail
from __future__ import division
import math

h = 0
t = 1
head = 0
tail = 0
count = 0
# Doubt: prob(head) and prob(tail) are half for both
# But from this training set the prob will be different
# How do we differentiate between these two entropy values
my_list = [h, h, t, h, h, t, h, h, t, h, h, t, h, h, h]

for i in my_list:
    if i == h:
        head += 1
    if i == t:
        tail += 1
    count += 1

prob_h = float(head / count)
prob_t = float(tail / count)

print(count)
print(prob_h)
print(prob_t)
# Entropy1 and Entropy2 are same for events with two possible outcomes
# Note: The value for 0log0 should be assigned as 0
entropy1 = -((prob_h * math.log(prob_h, 2)) + (prob_t * math.log(prob_t, 2)))
entropy2 = -((prob_h * math.log(prob_h, 2)) + ((1 - prob_h) * math.log(1 - prob_h, 2)))
print(entropy1)
print(entropy2)

