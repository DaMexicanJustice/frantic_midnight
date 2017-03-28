import pandas as pd
import os
import urllib.request as req
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import heapq

data = pd.read_csv('Aviation.csv', quotechar='"',skipinitialspace=True, delimiter=',', encoding='ISO-8859-2')

def ex5_dict_of_Destroyed(data):
    dead = {}
    for row in data.itertuples():
        temp = 0
        if row[4] < '1993-01-01': continue
            
        if pd.notnull( row[24] ):
            temp += row[24]
            
        if (row[12] == "Destroyed" or row[12] == 'Substantial' in dead):
            dead[row[4][0:4]] = temp
        else:
            dead.setdefault(row[4][0:4], temp)
    
    return dead

def dict_keys(d):
    return list(d.keys())

def dict_values(d):
    return list(d.values())
    
def plot(key, value):
    plt.bar(range(len(value)), value, width=0.5, linewidth=0, align='center')
    plt.xticks(range(len(value)), key, size='small')
    title = 'Dead over the years'
    plt.title(title, fontsize=20)
    plt.xlabel("years", fontsize=16)
    plt.ylabel("severity", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()
    
dead_dict = ex5_dict_of_Destroyed(data)
key = dict_keys(dead_dict)
value = dict_values(dead_dict)
plot(key, value)