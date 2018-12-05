import numpy
import pandas
import math
import sys
from math import sqrt
import random
#import sqrt

# def nearestneighbor():
#     print("in nn")

#attributes is the data stuff..

def distancefunc(x, y):
    distance = 0
    for i in range(len(x)):
        distance += float(pow(float(x[0])-float(y[0]), 2)) #cast all to float?
    distance = sqrt(distance)
    bestsofaracc = 0
    #print("Distance: ", distance)
    return distance
def findAccuracy(minval):
    print("hello")

def findnearest(attributes, label): #finding the nearestneighbor
    currentset = [] #empty array for the current set of features that exist
    minval = sys.maxsize
    accuracy = 0
    inc = 0
    #finding the distance between the two points
    for i in range(len(attributes)):
        for j in range(len(attributes)):
            currdist = distancefunc(attributes[i], attributes[j])
            if i != j and minval > currdist:
                #print(minval)
                minIndex = j
                minval = currdist
        if label[i] == label[minIndex]:
            inc+=1
    print(inc/len(attributes))
    return inc / len(attributes)
    currentset.append(minval)
    print("The array with all min vals: ")
    print(currentset)

def intersectfunc(dataarray, val):
    for i in range(len(dataarray)):
        # print(i , "VALSSSSS " , data[i], " ")
        if (dataarray[i] == val):
            return False
    return True

def featuresearch(data, attributes, label): #finding accuracy
    current_set_of_data  = []
    for i in range(len(data.columns)-1):
        print("On level ", i+1, " Of the search tree")
        feature_to_add_to_level = []
        best_so_far_accuracy = 0

        for k in range(len(data.columns)-1):
            if (intersectfunc(current_set_of_data, k)):
                print("--Considering adding the ", k+1, " feature--")
                # print(intersectfunc(current_set_of_data,k))
                accuracy = leave_one_out_of_cross_validation(attributes,label, current_set_of_data,k+1)
                if (accuracy > best_so_far_accuracy):
                    best_so_far_accuracy = accuracy
                    feature_to_add_to_level = k
        #print("Feature to add: ", feature_to_add_to_level)
        current_set_of_data.append(feature_to_add_to_level) #need to add one later?????
        print(current_set_of_data)

#currposition is the k+1 value
#find the accuracy of the nearestneighbor
def leave_one_out_of_cross_validation(attributes,label, current_set_of_data, currposition):
    accuracy =0#random.randint(1,100)
    #Used the random for testing features as per Keoghs reccomendations
    counter = 0
    findnearest(attributes, label)
    return accuracy

def main():
    print("in main")
    print("Welcome to Neesha Bhardwaj's Feature Selection Algorithm")
    names = ['class', 'afeat', 'bfeat', 'cfeat', 'dfeat', 'efeat', 'ffeat', 'gfeat', 'hfeat', 'ifeat', 'jfeat']

    data = pandas.read_csv("CS170_SMALLtestdata__110.txt", delim_whitespace=True, names = names)
    #print(data.head())
    #1: means from 1 to the end
    #originally had this:
    #attributes = data.iloc[:, 1].values#i.values
    attributes = data.iloc[:, 1:].values#i.values
    label = data.iloc[:,0].values
    #attributes = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    #attributes = [[0,0,0,0,0,0], [1,1,1,0,0,0], [1,1,1,1,1,1], [1,0,1,0,0,0]]
    print(attributes[0])
    #distancefunc(attributes[0],attributes[1])
    #findnearest(attributes)
    featuresearch(data, attributes, label)
    #print(y)

if __name__ == '__main__':
    main()
