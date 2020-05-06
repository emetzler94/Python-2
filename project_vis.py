# -*- coding: utf-8 -*-
"""
Eric Metzler
Python 2
5/3/20

Continuation of BTVA Webscrape.

5/3/20 Goal:  Read in CSV and create a histogram of each VA's credit count.
5/4/20 Goal:  Try to get a timeseries chart of two VA's careers.
Apparently this is ridiculously difficult...
5/5/20 Goal:  Attempt the same thing as yesterday.  Tinkering with pandas, I
think I lost my way.
"""

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np



df = pd.read_csv('va_data.csv')
df = df[df.year != 'TBA']


def comboChart(actorname):
    """
        Given an actor's name, creates a line and bar combination chart of
        their roles over the years.
    """
    #Creates a new dataframe from the original dataframe where the value
    #in the 'va' column is the actor's name.
    frame = df[df.va == actorname]
    print(frame.head())
    
    #Further focuses the dataframe to only include roles and years.
    frame = frame[['role', 'year']]
    print(frame.head())
    
    #Creates a multiple index table first indexed by year, then role. Column
    #is filled with the counts of each role per year.
    frame = frame.groupby(['year'])['role'].value_counts()
    print(frame.head())
    
    #Unstacks the indexes, creating a table where the rows are years, and the
    #columns are role types.  Resulting table has cells with no data filled in
    #with NaN, so fillna will replace them with 0.
    frame = frame.unstack('role').fillna(0)
    print(frame.head())
    
    #Creates a final column that has the sum of each row.
    frame.loc[:, 'total'] = frame.sum(axis=1)
    return frame

def plotComboChart(frame):
    exclusion = ['total']
    plt.axis(xlim=(frame.index.min(), frame.index.max()),
             ylim=(frame.total.min(), frame.total.max()))
    #we want to plot bars for each column except 'total', so we plot the same
    #graph except with 'total' being excluded
    frame.loc[:, frame.columns.difference(exclusion)].plot(kind='bar')    
    frame['total'].plot(kind='line')
    plt.ylabel('credit count')
    return frame

vaPlot = comboChart('Dan Castellaneta')
plotComboChart(vaPlot)