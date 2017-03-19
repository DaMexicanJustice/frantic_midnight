import webget
import pandas as pd
import matplotlib.pyplot as plt
import heapq
import os
from urllib.parse import urlparse
import re
import math

def download(url):
    #webget.download(url)
    #return os.path.basename(urlparse(url).path)
    # Getting the csv file via webget from github downloads a malformed csv that contains HTML tags, so we have to do it manually
    return "./database.csv"

def read_from_csv(filename):
    data = pd.read_csv(filename)
    data_no_nan = set_missing_values_to_0(data)
    return data_no_nan

def set_missing_values_to_0(data):
    return data.fillna(0.0)

#Which country has the lightest satellite and how much does it weight?
def ex4_lightest_satellite(data):
    satellite_owner = ""
    satellite_owner_country = ""
    satellite_name = ""
    satellite_weight = 10000.0;
    #Row 341 has a blank 'white' empty space for no apparent reason. I hard code my way around it. Help?
    index = 0
    
    for row in data.iterrows():
        #Is the index a string? If yes, it contains non-digits we need to remove
        if type( row[1][16]) is str:
            #Call to method that handles stripping our entry using a regular expression
            temp = remove_non_digits_and_float_cast(row[1][16], index)
            #If the weight is 0, then it was one of the NaN values we handled and it doesn't count
            if temp == 0:
                pass
            else:
                #King of the Hill implementation
                if temp < satellite_weight:
                    satellite_name = row[1][0]
                    satellite_owner_country = row[1][1]
                    satellite_owner = row[1][2]
                    satellite_weight = temp
            index += 1
        else:
            #The entry is already a float, so we can apply our gymnastics immediately
            if row[1][16] != 0:
                if row[1][16] < satellite_weight:
                    satellite_name = row[1][0]
                    satellite_owner_country = row[1][1]
                    satellite_owner = row[1][2]
                    satellite_weight = row[1][16]
                index += 1
            else:
                pass
    #The answer to the question is stored in 3 variables        
    return satellite_owner_country + " is the country with the lightest satellite weighing in at: " \
    + str(satellite_weight) + " kilograms" + \
    ", called: " + satellite_name + ", belonging to the " + satellite_owner
    
def remove_non_digits_and_float_cast(rowstr, index):
    temp = re.sub("[^0-9]", "", rowstr)
    temp = temp.strip()
    if index != 341:
        temp = float(temp)
    else:
        temp = 0;
    return temp
                
url = 'https://github.com/DaMexicanJustice/frantic_midnight/blob/master/Hand-in%203/database.csv'
file = download(url)
data = read_from_csv(file)
result = ex4_lightest_satellite(data)
print(result)