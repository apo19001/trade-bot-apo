import pandas as pd
import csv
import numpy as np

import matplotlib.pyplot as plt

# loads all the information we want into a array of tuples
# source: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
# conversion from a .csv file into a tuple that we can use
def loadfile(filename):
    data = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]
    return data

# takes in tag, print outs the address of where it is located in the
# tuple
def getId(identifier):
    if identifier == "Date":
        return 0
    elif identifier == "Open":
        return 1
    elif identifier == "High":
        return 2
    elif identifier == "Low":
        return 3
    elif identifier == "Close":
        return 4
    elif identifier == "Adj Close":
        return 5
    elif identifier == "Volume":
        return 6
    print("ERROR: Tag doesn't exist")
    return -1

# data is a tuple that we can our information from
def getfilecol(data, tag):
    stuff = []
    #print(data[1][getId('Date')])
    for i in range (1, len(data)):
        stuff.append(data[i][getId(tag)])
    return stuff

# generate the scatter plot to calculate regression line (maybe?)
def scatterplot(x, y, xtitle, ytitle):
    plt.scatter(x, y)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()
    return

# return the average price of all the prices
def returnaverage(prices):
    total = 0
    for i in range(1, len(prices)):
        total += float(prices[i])
    print(total / len(prices))

# print certain columns in our csv file
def readcertaincol(data, list):
    print(pd.DataFrame(data, columns = list))
    return

# calculate the r^2 of our data set.
# source: https://www.kite.com/python/answers/how-to-calculate-r-squared-with-numpy-in-python
def r_squared(x, y):
    correlation_matrix = np.corrcoef(np.array(x).astype(np.int), np.array(y).astype(np.float))
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return r_squared

# return the r value closer it is to 1 the better the line we have!
def r(x,y):
    correlation_matrix = np.corrcoef(np.array(x).astype(np.int), np.array(y).astype(np.float))
    correlation_xy = correlation_matrix[0, 1]
    return correlation_xy

# return the regression line that we can model the stock prices with
# poly - the degree of the polynomial we want
# source: https://www.kite.com/python/answers/how-to-plot-a-linear-regression-line-on-a-scatter-plot-in-python
#         https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
def regression(x, y, poly):
    m, b = np.polyfit(x, y, 1)
    print("slope: ", str(m))
    print("y-intercept: ", str(b))
    
# print out regression line and the 
def info(x, y):
    print("r-value: ", str(r(x, y)))
    print("r^2: ", str(r_squared(x, y)))
    regression(np.array(x).astype(np.int), np.array(y).astype(np.float), 1)

# so we want a basic calculation - if we see the price is going down, we want
# to buy it when its low - we see a negative trend
def buyme(x, y):
    if (r(x, y) < 0):
        return True
    return False

# run through the backend calculations

"""
NOTES:

Read parts of the column
data = pd.read_csv('TSLA.csv')
df = pd.DataFrame(data, columns= ['Date', 'Close'])
"""
def main():
    obj = loadfile('TSLA.csv')
    dates = getfilecol(obj, 'Date')
    prices = getfilecol(obj, 'Close')
    x_axis = [date for date in range(len(dates))]
    scatterplot(x_axis, prices, 'Date', 'Close')
    info(x_axis, prices)

    
main()
