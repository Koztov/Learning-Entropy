import math

def cal(values, num):

        # Hartley entropy (not sure)
        print("When alpha=0: " + math.log(5, 2).__str__())

        # Shannon entropy
        sum = 0
        for i in range(0, num):
                sum += values[0][i] * math.log(values[0][i], 2)
        val = -sum
        print("When alpha=1: " + val.__str__())

        # collision entropy or Renyi_s quadratic entropy
        sum = 0
        for i in range(0, num):
                sum += math.pow(values[0][i], 2)
        val = -math.log(sum, 2)
        print("When alpha=2: " + val.__str__())
