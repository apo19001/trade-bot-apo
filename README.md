# trade-bot-apo

# Overview

I wanted to analyze a stock so that I would be able to predict its future price
to see if it was worth buying. I got the information from yahoo finance,
and I used numpy and matplotlib to show the prices on
a graph and found its regression line.

I then graded the accuracy of the regression line by calculating its 
r value (how well the line fits the data I have).

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

1) How can I predict the future prices on TSLA? I model the data.
 
  *  I found that the data I had was modeled by this regression line.
  *  price(x) = 2.278x + 243
  *  R^2 = 0.71

  * After grading our R^2 value, we found that it modeled our data moderately well (71%). It isn't the best model, but our line was able to somewhat model the prices within the last couple weeks well. Granted, I would probably look into more tests to model the prices better. 

2) Should I buy this stock?

  * I wanted to implement a way to grade the general trend of the line. 
  If I wanted to buy this stock, I wanted to see if there was a slope
  in the pricing, or a decrease. Since I found there was a positive
  trend in the data, I didn't want to buy the stock. 
# Development Environment

* I used EMACS to program this project.

* I used python 3.8.5.

## Python libaries used
* pandas
* csv
* numpy
* matplotlib


# Useful Websites
* [TSLA data] (https://www.marketwatch.com/investing/stock/TSLA/download-data?siteid=mktw&date=7%2F1%2F2021&x=16&y=3)
* [grading our regressiom line]( https://www.kite.com/python/answers/how-to-calculate-r-squared-with-numpy-in-python)
* [export csv file to list](https://stackoverflow.com/questions/24662571/python-import-csv-to-list)
* [Line of best fit analysis] (https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)
* [How to display line of best fit] (https://www.kite.com/python/answers/how-to-plot-a-linear-regression-line-on-a-scatter-plot-in-python)

# Future Work

* add paper trading
* work on finding better modeling techniques
* show picture of stock
