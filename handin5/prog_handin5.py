import pandas as pd
import matplotlib.pyplot as plt
import webget
from collections import defaultdict
from urllib.parse import urlparse
import os
import heapq

data_csv = "http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv"

def download(link):
    file = webget.download(link)
    return os.path.basename(urlparse(link).path)

def csv_to_df(src):
    return pd.read_csv(src)

def make_barplot(src, title="Untitled"):
    plt.bar(range(len(src)), src.values(), align='center')
    plt.xticks(range(len(src)), list(src.keys()))
    plt.title(title)
    plt.show()

def make_scatterplot(src, title="Untitled"):
    plt.scatter(list(src.keys()), list(src.values()), c=list(src.values()), cmap=plt.cm.Blues, edgecolor='none', s=40)
    plt.title(title)
    plt.show()

def make_plot(src, title="Untitled"):
    plt.plot(list(src.keys()), list(src.values()), linewidth=5)
    plt.title(title)
    plt.show()
    
def make_multiplot(src_list, my_labels, title="Untitled"):
    index = 0
    
    for src in src_list:
        plt.plot(list(src.keys()), list(src.values()), linewidth=5, label=my_labels[index])
        index += 1
    plt.title(title)
    plt.legend(loc="upper left", bbox_to_anchor=[0, 1],ncol=2, shadow=True, title="Legend", fancybox=True)
    plt.show()

def ex1(df):
    # creates default entries with a value of 0 in case of absent data
    
    males_18_30 = defaultdict(lambda: 0)
    females_18_30 = defaultdict(lambda: 0)
    males_50_above = defaultdict(lambda: 0)
    females_50_above = defaultdict(lambda: 0)
    
    for row in df.itertuples():
        
        if(int(row[1]) <= 2015 and int(row[1]) >= 1992):
            # column 5 is gender
            if row[5] == 1:
                if row[3] <= 30 and row[3] >= 18:
                    males_18_30[row[1]] += 1
                if row[3] >= 50:
                    males_50_above[row[1]] += 1
            else:
                if row[3] <= 30 and row[3] >= 18:
                    females_18_30[row[1]] += 1
                if row[3] >= 50:
                    females_50_above[row[1]] += 1
    # make_plot(males_18_30, "Amount of males from 18-30")
    
    make_multiplot([males_18_30, females_18_30, males_50_above, females_50_above],["males 18-30","females 18-30","males 50 above","females 50 above"], "Comparison")

def something_plot(dict_a, dict_b, label_a, label_b, name):
    males = list(dict_a.values())
    females = list(dict_b.values())
    indexes = list(dict_a.keys())
    
    p1 = plt.bar(indexes, females, width=0.5, color="#d62728")
    p2 = plt.bar(indexes, males, width=0.5, bottom=females)
    plt.title(name)
    plt.legend((p1, p2), (label_b, label_a))
    plt.show()

    
def ex2(df):
    city_part_1_m = defaultdict(lambda: 0)
    city_part_1_f = defaultdict(lambda: 0)
    
    city_part_2_m = defaultdict(lambda: 0)
    city_part_2_f = defaultdict(lambda: 0)
    
    city_part_3_m = defaultdict(lambda: 0)
    city_part_3_f = defaultdict(lambda: 0)
    
    for row in df.itertuples():
        if(int(row[1]) <= 2015 and int(row[1]) >= 1992):
            # lets assume unmarried means neither G nor P
            if(row[4] != "G" and row[4] != "P"):
                if row[3] <= 30 and row[3] >= 18:
                    if row[5] == 1: # male
                        if row[2] == 1:
                            city_part_1_m[row[1]] += 1
                        if row[2] == 2:
                            city_part_2_m[row[1]] += 1
                        if row[2] == 3:
                            city_part_3_m[row[1]] += 1
                    else: # female
                        if row[2] == 1:
                            city_part_1_f[row[1]] += 1
                        if row[2] == 2:
                            city_part_2_f[row[1]] += 1
                        if row[2] == 3:
                            city_part_3_f[row[1]] += 1
    
    something_plot(city_part_1_m, city_part_1_f, "Male", "Female", "Bydel 1, 18-30")
    something_plot(city_part_2_m, city_part_2_f, "Male", "Female", "Bydel 2, 18-30")
    something_plot(city_part_3_m, city_part_3_f, "Male", "Female", "Bydel 3, 18-30")
    
    make_multiplot(
        [
            city_part_1_m,
            city_part_1_f,
            city_part_2_m,
            city_part_2_f,
            city_part_3_m,
            city_part_3_f
        ]
        ,[
            "males 18-30 | Bydel 1",
            "females 18-30 | Bydel 1",
            "males 18-30 | Bydel 2",
            "females 18-30 | Bydel 2",
            "males 18-30 | Bydel 3",
            "females 18-30 | Bydel 3",
        ]
        , "Comparison"
    )
    
def lookup_citypart(n):
    res = []
    
    parts = {
        1: "Indre By",
        2: "Østerbro",
        3: "Nørrebro",
        4: "Vesterbro/Kgs. Enghave",
        5: "Valby",
        6: "Vanløse",
        7: "Brønshøj-Husum",
        8: "Bispebjerg",
        9: "Amager Øst,",
        10: "Amager Vest",
        99: "Udenfor inddeling"
    }
    
    for x in n:
        res.append(parts[x])
    return res
        
        
def get_n_largest(d, n):
    return heapq.nlargest(n, d, key=d.get)
    
def ex3(df):
    winner_1992 = defaultdict(lambda: 0)
    winner_2000 = defaultdict(lambda: 0)
    winner_2015 = defaultdict(lambda: 0)
    
    for row in df.itertuples():
        if row[1] == 1992:
            winner_1992[row[2]] += 1
        if row[1] == 2000:
            winner_2000[row[2]] += 1
        if row[1] == 2015:
            winner_2015[row[2]] += 1
     
    print("Top 3 City parts by population in 1992: " + str(lookup_citypart(get_n_largest(winner_1992, 3))))
    print("Top 3 City parts by population in 2000: " + str(lookup_citypart(get_n_largest(winner_2000, 3))))
    print("Top 3 City parts by population in 2015: " + str(lookup_citypart(get_n_largest(winner_2015, 3))))
    
                 
downloaded_file = download(data_csv)
data_frame = csv_to_df(downloaded_file)

#ex1(data_frame)
#ex2(data_frame)
ex3(data_frame)