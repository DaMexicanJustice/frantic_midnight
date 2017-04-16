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
    
def hist_plot1(K, V):
    plt.bar(K, V, width=0.5, linewidth=0, align='center')
    plt.ticklabel_format(useOffset=False)
    plt.axis([0, max(K) + 10, 0, 1800])
    title = 'Rating histogram'
    plt.title(title, fontsize=20)
    plt.xlabel("Rating", fontsize=20)
    plt.ylabel("Rating Amount", fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.savefig("Rating.jpg")
    plt.show()
    
    
def hist_plot2(K, V):
    plt.bar(K, V, width=0.5, linewidth=0, align='center')
    plt.ticklabel_format(useOffset=False)
    plt.axis([0, max(K) + 10, 0, 1300])
    title = 'Length histogram'
    plt.title(title, fontsize=20)
    plt.xlabel("Length", fontsize=20)
    plt.ylabel("Length Amount", fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.savefig("Length.jpg")
    plt.show()
    
    
def hist_plot3(K, V):
    plt.bar(K, V, width=0.5, linewidth=0, align='center')
    plt.ticklabel_format(useOffset=False)
    plt.axis([0, max(K) + 10, 0, 1300]) #Giver valueError, max() arg is an empty sequence
    title = 'Title length histogram'
    plt.title(title, fontsize=20)
    plt.xlabel("titles", fontsize=20)
    plt.ylabel("Length", fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.savefig("Length_of_title.png")
    plt.show()
    


# Rating=5, Length=3, title=1    
def ex_one(data):
    rating_dict = defaultdict(lambda: 0)
    length_dict = defaultdict(lambda: 0)
    title_dict = defaultdict(lambda: 0)
    
    for row in data.itertuples():
        rating = row[6]
        length = row[4]
        title = row[2]
        year = row[3]
        
        if rating in rating_dict:
            rating_dict[rating] += 1
        else:
            rating_dict[rating] = 1
        
        if length in length_dict:
            length_dict[length] += 1
        else:
            length_dict[length] = 1
            
        if year in title_dict:
            if title in title_dict:
                title_dict[length] += 1 #Hvad gør jeg forkert?
            
    hist_plot1(list(rating_dict.keys()), list(rating_dict.values()))
    hist_plot2(list(length_dict.keys()), list(length_dict.values()))
    hist_plot3(list(title_dict.keys()), list(title_dict.values())) # :/
    
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
ex_one(data)
#movie_dict = ex_two(data)
#d_keys = get_dict_keys(movie_dict)
#d_values = get_dict_values(movie_dict)
#bar_plot(d_keys, d_values)