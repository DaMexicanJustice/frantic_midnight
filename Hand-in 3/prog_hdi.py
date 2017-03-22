import pandas as pd
from collections import defaultdict

countries = defaultdict(lambda: 0.0)

data = pd.read_csv("./historical_index.csv")


for row in data.itertuples():
	if(row[3] != ".."):
		countries[row[2]] += float(row[9])-float(row[3])

best = max(countries, key=countries.get)
print(best + " with " + str(dict(countries)[best]))

#country = 1
#1990 = 2
#2014 = 8
