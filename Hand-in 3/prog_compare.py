import pandas as pd
from collections import defaultdict

countries = defaultdict(lambda: 0.0)
hdi_data = pd.read_csv("HDI.csv")

allHDI = []

def fix_val(_in):
    if "," not in _in:
        return float(row[7])/1000.0
    else:
        return float(row[7].replace(",","."))

for row in hdi_data.itertuples():
    allHDI.append(fix_val(row[7]))

allHDI.sort()

rich_countries = defaultdict(lambda: 0)
poor_countries = defaultdict(lambda: 0)

top5rich = []
top5poor = []

for row in hdi_data.itertuples():
    val = fix_val(row[7])
    if(val >= allHDI[-5]):
        top5rich.append(row[2])
        rich_countries[row[2]] = 1
    if(val < allHDI[5]):
        top5poor.append(row[2])
        poor_countries[row[2]] = 1


sattelite_data = pd.read_csv("satellites.csv")

rich_sat_usage = defaultdict(lambda: 0)
poor_sat_usage = defaultdict(lambda: 0)

for row in sattelite_data.itertuples():
    if(rich_countries[row[4]] == 1):
        rich_sat_usage[row[5]] += 1
    if(poor_countries[row[4]] == 1):
        poor_sat_usage[row[5]] += 1

print("Top 5 rich countries are:")
print(top5rich)
print("Top 5 rich countries use sattelites for:")
print(dict(rich_sat_usage))


print("Top 5 poor countries are:")
print(top5poor)
print("Top 5 poor countries use satellites for:")
print(dict(poor_sat_usage))
