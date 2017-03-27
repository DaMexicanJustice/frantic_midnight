import pandas as pd
import os
import urllib.request as req
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import heapq

data = pd.read_csv('Aviation.csv', quotechar='"',skipinitialspace=True, delimiter=',', encoding='ISO-8859-2')

def ex2_dict_of_injuries(data):
    # location 4
    # Country 5
    # Total.Serious.Injuries 24
    # Total.Minor.Injuries 25
    country = {}
    for row in data.itertuples():
        temp = 0
        if pd.notnull( row[25] ):
            temp += row[25]
        if pd.notnull( row[26] ):
            temp += row[26]
            
        if (row[6] == "United States" in country):
            country[row[5]] = temp
        else:
            country.setdefault(row[6], temp)
    
    return country

def top(d, n=None):
    li = heapq.nlargest(n, d, key=d.get) 
    di = {}
    for ac in li:
        di[ac] = d.get(ac)
    return di

def dict_keys(d):
    return list(d.keys())

def dict_values(d):
    return list(d.values())
    
def plot(key, value):
    plt.bar(range(len(value)), value, width=0.5, linewidth=0, align='center')
    plt.xticks(range(len(value)), key, size='small')
    title = 'Most major and minor injuries in US states'
    plt.title(title, fontsize=20)
    plt.xlabel("US States/Locations", fontsize=12)
    plt.ylabel("Injuries", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=7)
    plt.show()
    
injury_dict = ex2_dict_of_injuries(data)
top_5 = top(injury_dict,5)
key = dict_keys(top_5)
value = dict_values(top_5)
plot(key, value)