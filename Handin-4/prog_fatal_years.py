import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import math

years_dict = defaultdict(lambda: 0)
aviation_data = pd.read_csv("AviationDataset.csv", encoding='ISO-8859-2')

for row in aviation_data.itertuples():
    tmp = row[4][0:4]
    
    
    if(math.isnan(row[24]) == False and tmp > '1997-01-01'):
        years_dict[tmp] += row[24]

plt.bar(range(len(years_dict)), years_dict.values(), align='center')
plt.xticks(range(len(years_dict)), list(years_dict.keys()))

plt.show()