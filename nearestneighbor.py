import numpy
import pandas

def nearestneighbor():
    print("in nn")


def main():
    print("in main")
    names = ['class', 'afeat', 'bfeat', 'cfeat', 'dfeat', 'efeat', 'ffeat', 'gfeat', 'hfeat', 'ifeat', 'jfeat']

    data = pandas.read_csv("CS170_SMALLtestdata__52.txt", delim_whitespace=True, names = names)
    print(data.head())





if __name__ == '__main__':
    main()
