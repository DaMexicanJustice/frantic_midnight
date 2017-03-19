import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Which country has the highest HDI and which has the lowest?
#country 1, HDI 2.

HDIs = pd.read_csv("HDI.csv")

dd = HDIs.as_matrix()

countries = np.unique(dd[:,1])
HDI = np.unique(dd[:,2])

country = np.array([np.sum(dd[(dd[:,1] == count)][:,2]) for count in countries])

print("Country with highest HDI: " + countries[np.argmax(country)], np.amax(HDI))
print("Country with lowest HDI: " + countries[np.argmin(country)], np.amin(HDI))