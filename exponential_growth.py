#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:13:46 2020

@author: hteza
"""

# obsolete
# will not be maintained

## source = https://jooskorstanje.com/modeling-exponential-growth-corona.html
## refer this for exponential formula https://www.youtube.com/watch?v=Kas0tIxDvrg&t=35s
## Dataset - Myanmar COVID 19 Dataset by Dr. Nyein Chan Ko Ko

# exponential formula -> y=a * b**x
# a -> original value
# b -> rate of chnage -> (1+r)[growth rate] or (1-r)[decay rate]
# r -> the ratio of today to yesterday

import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# please update the dictionary for future cases
# in cummulative form
Myanmar = {"3/21/20" : 1,
           "3/22/20" : 1,
           "3/23/20" : 3,
           "3/24/20" : 3,
           "3/25/20" : 5,
           "3/26/20" : 8,
           "3/27/20" : 8}

confirmed_df = pd.DataFrame(list(Myanmar.items()),columns = ["Date","Case"]) 
confirmed_df["Date"] = pd.to_datetime(confirmed_df["Date"])
confirmed_df["ndays"] = np.arange(len(confirmed_df))

####################################################

# Natural Log of Real Cases
confirmed_df["logCase"] = np.log(confirmed_df.Case).astype(float)

# Linear Regression
X = confirmed_df.ndays
X = sm.add_constant(X)
y = confirmed_df.logCase
model = sm.OLS(y, X)
result = model.fit()

####################################################

# Exponential  function -> 
# y = initial value * rate of change ** day

# y = np.exp(result.params["const"]) * np.exp(result.params["ndays"]) ** t

def linear_predictions(t):
    # we want real number predicted, so exponent by e again
    return np.exp(result.params["const"]) * np.exp(result.params["ndays"]) ** t

####################################################

# next week prediction
ndays = len(confirmed_df)+3
nextweek_df = pd.DataFrame(columns=["ndays","Date"])
nextweek_df["ndays"] = np.arange(ndays)
nextweek_df.loc[0,"Date"]=confirmed_df.loc[0,"Date"]
for i in range(1,len(nextweek_df)):
    nextweek_df.loc[i,"Date"] = nextweek_df.loc[i-1,"Date"] + pd.Timedelta(days=1)
    i=i+1
nextweek_df["Predictions"] = nextweek_df.ndays.apply(linear_predictions)
# Natural Log of Predicted Cases
nextweek_df["logPredictions"] = np.log(nextweek_df.Predictions).astype(float)


####################################################

# Real Number Plot

confirmed_x = pd.date_range(start=confirmed_df["Date"][confirmed_df.index[0]], end=confirmed_df["Date"][confirmed_df.index[-1]])
confirmed_y = confirmed_df["Case"].tolist()
confirmed_plot = pd.Series(data=confirmed_y, index=confirmed_x)

nextweek_x = pd.date_range(start=nextweek_df["Date"][nextweek_df.index[0]], end=nextweek_df["Date"][nextweek_df.index[-1]])
nextweek_y = nextweek_df["Predictions"].tolist()
nextweek_plot = pd.Series(data=nextweek_y, index=nextweek_x)

fig, ax = plt.subplots()
ax.plot(confirmed_plot, label="Confirmed", color="red")
ax.plot(nextweek_plot, label="Predicted", color ="blue")
legend = ax.legend(loc="top left", fontsize="large")
plt.xlabel("Date")
plt.ylabel("Infections")
plt.suptitle("Predicted number of cases vs real number of cases")
plt.title("As of "+str(confirmed_df["Date"][confirmed_df.index[-1]]))
plt.xticks(rotation=90)
plt.show()


####################################################

# Natural Log Plot

confirmed_logy = confirmed_df["logCase"].tolist()
confirmed_logplot = pd.Series(data=confirmed_logy, index=confirmed_x)

nextweek_logy = nextweek_df["logPredictions"].tolist()
nextweek_logplot = pd.Series(data=nextweek_logy, index=nextweek_x)

fig, ax = plt.subplots()
ax.plot(confirmed_logplot, label="Confirmed", color="red")
ax.plot(nextweek_logplot, label="Predicted", color ="blue")
legend = ax.legend(loc="top left", fontsize="large")
plt.xlabel("Date")
plt.ylabel("Infections")
plt.suptitle("Predicted number of cases vs real number of cases (Natural Log)")
plt.title("As of "+str(confirmed_df["Date"][confirmed_df.index[-1]]))
plt.xticks(rotation=90)
plt.show()


####################################################
