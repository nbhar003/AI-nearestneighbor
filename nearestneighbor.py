import numpy
import pandas
import math
from math import sqrt

def nearestneighbor():
    print("in nn")

def distancefunc(x, y):
    for i in range(len(x)):
        distance += pow(x[i]-y[i], 2)
        distance = sqrt(distance)
    print("Distance: ", distance)

def main():
    print("in main")
    print("Welcome to Neesha Bhardwaj's Feature Selection Algorithm")
    names = ['class', 'afeat', 'bfeat', 'cfeat', 'dfeat', 'efeat', 'ffeat', 'gfeat', 'hfeat', 'ifeat', 'jfeat']

    data = pandas.read_csv("CS170_SMALLtestdata__52.txt", delim_whitespace=True, names = names)
    #print(data.head())
    #1: means from 1 to the end
    attributes = data.iloc[:, 1:]#i.values
    label = data.iloc[:,0].values
    print(attributes)
    distancefunc(attributes[0],attributes[1])
    #print(y)


if __name__ == '__main__':
    main()
