import pandas as pd
import matplotlib.pyplot as plt
import webget
from collections import defaultdict
from urllib.parse import urlparse
import os

url = "http://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/movies.csv"

def download(link):
    file = webget.download(link)
    return os.path.basename(urlparse(link).path)

def csv_to_df(src):
    return pd.read_csv(src)

# Plot the years on the x-axis and all the movies and their duration/length on the y-axis. Multiple values for y, one for x. X&y size mistmatch?
def scatter_three(keys, values, title="Untitled"):
    pass

def bar_plot(keys, values):
    plt.bar(keys,values)
    plt.show()
    plt.savefig("movies_released_by_year.png")

def ex_three(data):
    movie_dict = defaultdict(lambda: 0)
    
    for row in data.itertuples():
            if row[3] in movie_dict.keys():
                # THIS IS HOW IT'S DONE! :D :D :D :D :D !!!!! :D ;))
                movie_dict[row[3]][row[2]] = row[4]
            else:
                movie_dict[row[3]] = {row[2] : row[4]}
                
    return movie_dict

def ex_two(data):
    movie_dict = defaultdict(lambda:0)
    
    for row in data.itertuples():
        year = row[3]
        if year in movie_dict:
            movie_dict[year] += 1
        else:
            movie_dict[year] = 1
            
    return movie_dict

# Returns all the years
def get_dict_keys(d):
    return list(d.keys())

def get_dict_values(d):
    return list(d.values())

# Should return all the values for movie length/duration. Dict structure: {year : {title : length } }
# How to get the values for length, without losing track of which year it is?
def get_sub_dict_values(d):
    sd_values = []
    for row in d.values():
        sd_values.append(list(row.values()))
    return sd_values
    
file = download(url)
data = csv_to_df(file)
movie_dict = ex_two(data)
d_keys = get_dict_keys(movie_dict)
d_values = get_dict_values(movie_dict)
bar_plot(d_keys, d_values)