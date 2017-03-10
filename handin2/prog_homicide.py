import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
def ex3_women_weapon(data):
    pass

# What is the age of the youngest victim and the oldest victim?
def ex4_youngest_oldest_victim(data):
    pass

# Average age of victims?
def ex5_average_victim_age(data):
    pass

# Male to female ratio of perpetrators?
def ex6_gender_ratio_attackers(data):
    pass

# Top 10 states with most homicides? display it with bars (barchart) or similar
def ex7_states_most_homicides(data):
    pass

# Are younger perpetrators (age 15-25) more likely to get caught then older ones (25+)?
def ex8_bonus(data):
    pass

filename = download("fakeurl")
data = read_from_csv(filename)
