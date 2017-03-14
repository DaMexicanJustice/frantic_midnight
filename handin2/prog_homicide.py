import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pprint
import heapq
# import webget

# todo: make not fake
def download(url):
    return "./database.csv"

def read_from_csv(filename):
    data = pd.read_csv(filename)
    return data

# Which ethnicity is it most common for the victims and perpetrators to be?
def ex1_ethnicities(data):
    pass

# Which weapon is most used by men?
def ex2_most_popular_weapons(data):
    pass

# Which weapon is most used by women?
def ex3_women_weapon():

    homicides = pd.read_csv("database.csv", dtype={"Perpetrator Age": object})

    dd = homicides.as_matrix()

# Weapon = 20
# Perpetrator sex = 15

    weapons, count = np.unique(dd[(dd[:,15] == "Female")][:,20], return_counts=True)
    return weapons[np.argmax(count)]
    
print("Most used weapon by females: " + ex3_women_weapon())

# What is the age of the youngest victim and the oldest victim?
def ex4_youngest_victim():
    homicides = pd.read_csv("database.csv", dtype={"Perpetrator Age": object})

    dd = homicides.as_matrix()
    
    young_victim = np.unique(dd[:,12])
    return np.argmin(young_victim)

def ex4_oldest_victim():
    homicides = pd.read_csv("database.csv", dtype={"Perpetrator Age": object})

    dd = homicides.as_matrix()
    
    old_victim = np.unique(dd[:,12])
    return np.argmax(old_victim)


print("Youngest victim: ", ex4_youngest_victim(), "years old")
print("Oldest victim: ", ex4_oldest_victim(), "years old")

# Average age of victims?
def ex5_average_victim_age(data):
    pass

# Male to female ratio of perpetrators?
def ex6_gender_ratio_attackers(data):
    pass

# Top 10 states with most homicides? display it with bars (barchart) or similar
def ex7_states_most_homicides(data, limiter):
    if limiter > len(data):
        raise ValueError('Limiter value higher than data in dataset!')
    states = {}
    for idx, row in data.iterrows():
        if row["State"] in states:
            states[row["State"]] += 1
        else:
            states.setdefault(row["State"], 0)
        if idx > limiter:
            break
    top_10_states = {}
    #Return the top 6 elements in our list. nlargest takes n = elements, iterable = Publishers and opt key which we need here 
    list_of_states = heapq.nlargest(10, states, key=states.get) 
    for state in list_of_states:
        top_10_states[state] = states.get(state)
    return top_10_states
        
def ex7_plot(tt_values, tt_labels):
    plt.bar(range(len(tt_values)), tt_values, width=0.5, linewidth=0, align='center')
    plt.xticks(range(len(tt_values)), tt_labels, size='small')
    title = 'Top 10 states with highest recorded homocide rates'
    plt.title(title, fontsize=20)
    plt.xlabel("State", fontsize=12)
    plt.ylabel("No. of homocide cases", fontsize=12)
    plt.tick_params(axis='x', which='major', labelsize=5)
    plt.show()
    
# Are younger perpetrators (age 15-25) more likely to get caught then older ones (25+)?
def ex8_bonus(data):
    pass

filename = download("fakeurl")
data = read_from_csv(filename)
top_ten_states = ex7_states_most_homicides(data, len(data))
tt_labels = list(top_ten_states.keys())
tt_values = list(top_ten_states.values())
ex7_plot(tt_values, tt_labels)