import math

def cal(p_values, q_values, num):

        pq_sum = 0
        for i in range(num):
            pq_sum += q_values[0][i]
        val = -math.log(pq_sum, 2)
        print("For alpha=1: " + val.__str__())

        # Kullback_Leibler divergence, which is the
        # information distance commonly used for detecting
        # DDoS attacks
        pq_sum = 0
        for i in range(num):
            pq_sum += p_values[0][i] * math.log(p_values[0][i] / q_values[0][i], 2)
        val = pq_sum
        print("For alpha=1: " + val.__str__())

        pq_sum = 0
        for i in range(num):
            pq_sum += math.pow(p_values[0][i], 2) / q_values[0][i]
        val = math.log(pq_sum, 2)
        print("For alpha=2: " + val.__str__())
