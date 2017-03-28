import webget
import pandas as pd
import os
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import io
import requests

url = 'https://raw.githubusercontent.com/edipetres/Depressed_Year/master/Dataset_Assignment/AviationDataset.csv'
s = requests.get(url).content
data =pd.read_csv(io.StringIO(s.decode('ISO-8859-2')), delimiter=',', quotechar='"')

    

def distribution_of_fatalities(data):
    distribution = {}
    
    for row in data.iterrows(): 
        
        phase_of_flight = 'UNKNOWN'
        fatalities = 0
        
        if pd.isnull(row[1][28]):
            pass
        else:
            phase_of_flight = (row[1][28])
            
        try:
            fatalities = int(row[1][23])
        except ValueError:
            pass        
            
            
        if (phase_of_flight not in distribution.keys()):
            distribution[phase_of_flight] = fatalities
        else:
            distribution[phase_of_flight] += fatalities
    
    sorted_keys = sorted(distribution, key=distribution.get) 
    
    fatal_list = list(distribution.values())        
    flight_phases = list(distribution.keys())
    
    title = 'How do the flight phases contribute to fatalities?'
    plt.title(title, fontsize=16)
    
    plt.xlabel("Flight Phase", fontsize=11)
    plt.ylabel("Number of fatalities", fontsize=11)
    plt.bar(range(len(distribution)), distribution.values(), width=0.75, linewidth=0.5, align='center')
    plt.xticks(range(len(distribution)), flight_phases)
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    
    
    #plt.bar(flight_phases, fatal_list, width=0.8, linewidth=0.5, align='center')
    #my_xticks = sorted_keys.keys()
    #plt.xticks(flight_phases, my_xticks)
    #plt.tick_params(axis='both', which='major', labelsize=10)
    
distribution_of_fatalities(data)