# generate N observations from normal dist
# data = rand(N,1);
#   1 = standard dev.
#   mu = mean = 0
# estimate the mean and variance of the data for N = 10,100,1000
#
# Modify code so that the generated data have mean and variance
# equal to user specified parameters mean and var.
#
import numpy as np
import math
#PART 1
# doesnt take user input to specify the mean or number of elements
def observations():
        nd = np.random.normal(0, 1, (1000, 1))
        nd2 = np.random.normal(0, 1, (100, 1))
        nd3 = np.random.normal(0, 1, (100, 1))

    print("-----------------------X------------------------")
    print(x)
    print("-----------------------Y------------------------")
    print(y)
    print("-----------------------Z------------------------")
    print(z)
    print("------------------------------------------------")


#function that takes user input to specify mean and variance and number of values
def observationsUI(mean, var, N):
    mean = input("Enter the mean value: ")
    var = input("Enter the variance: ")
    N = input("Enter the number of elements: ")
        ndT = np.random.normal(mean, math.sqrt(var), (N, 1))
        ndT.append(ax)

    estimated_mean = ax.sum / 3000
    estimated_variance = ((ax - estimated_mean)**2).sum / 3000-1

    print("---------------------AX------------------------")
    print(ax)
    print("-----------------------------------------------")



#PART 2
