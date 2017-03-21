import pandas as pd
import numpy as np
import operator
import matplotlib.pyplot as plt 

data = pd.read_csv("./database.csv")

def military_satellites(data):

    country_m = {} 
    
    for row in data.iterrows():
        if(row[1][3] in country_m):
            pass
        else:
            country_m.setdefault(row[1][3], 0)
            

    for row in data.iterrows():
        if (row[1][4] == "Military"):
            temp = row[1][3]
            country_m[temp] = country_m.get(temp, 0) + 1
                        
            
            
    maximum = max(country_m, key=country_m.get) 
    print("Country with the most satellites used for military purposes is: ") 
    print(maximum + "with a total of: " + str(country_m[maximum]) + " satellites.")

military_satellites(data)