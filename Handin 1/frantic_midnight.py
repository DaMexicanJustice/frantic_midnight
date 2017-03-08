import webget
import csv
from urllib.parse import urlparse
import os
import matplotlib.pyplot as plt
import heapq

url = "https://raw.githubusercontent.com/DaMexicanJustice/frantic_midnight/master/data%20sets/vgsales.csv"

def download(url):
    webget.download(url)
    return os.path.basename(urlparse(url).path)
#Patrick
def find_most_pop_platform_by_regions(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        _ = next(reader)
        
        EU = {}
        NA = {}
        JP = {}
    
        for row in reader:
            if(row[6] == "NA_Sales"):
                pass # ignore headers
            else:
                NA.setdefault(row[2], 0)
                NA[row[2]] += float(row[6])
            
                EU.setdefault(row[2], 0)
                EU[row[2]] += float(row[7])
            
                JP.setdefault(row[2], 0)
                JP[row[2]] += float(row[8])
        #pop_list = ("Most popular in EU: " + str(max(EU, key=EU.get)),"Most popular in NA: " + str(max(NA, key=NA.get)),"Most popular in JP: " + str(max(JP, key=JP.get)) )
        
        na_key = str( max(NA, key=NA.get) ) + "\n(NA)"
        na_val = NA[row[2]]
        eu_key = str( max(EU, key=EU.get) ) + "\n(EU)"
        eu_val = EU[row[2]]
        jp_key = str( max(JP, key=JP.get) ) + "\n(JP)"
        jp_val = JP[row[2]]
        
        pop_list = {na_key : na_val, eu_key : eu_val, jp_key : jp_val}
        return pop_list
        
#Michael    
def find_sum_of_all(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        _ = next(reader)
        
        NA_Sum = 0;
        EU_Sum = 0;
        JP_Sum = 0;
        Other_Sum = 0;
        Global_Sum = 0;
        
        for row in reader:
            if(row[6] == "NA_Sales"):
                pass # ignore headers
            else:
                NA_Sum += float(row[6])
                EU_Sum += float(row[7])
                JP_Sum += float(row[8])
                Other_Sum += float(row[9])
                Global_Sum += float(row[10])
        
        regionSales = {"NA": NA_Sum, "EU": EU_Sum, "JP": JP_Sum, "Other": Other_Sum}
        
        #print("NA sum of global: " + str(100*NA_Sum/Global_Sum)+"\n" + " EU sum of global: " + str(100*EU_Sum/Global_Sum)+"\n" + " JP sum of global: " + str(100*JP_Sum/Global_Sum)+"\n" + " Other_countries sum of global: " + str(100*Other_Sum/Global_Sum))
        
        return regionSales
    
#Martin
def genres2012(filename):
    genres2012 = {}
    publishers = {}
 
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            if(row[6] == "NA_Sales"):
                pass
            else:
                genres2012.setdefault(row[4], 0)
                if(row[3] == "2012"):
                    genres2012[row[4]] += float(row[10])
            
                publishers.setdefault(row[5], 0)
                publishers[row[5]] += 1
    return genres2012
    return str(max(genres2012, key=genres2012.get))

#Lasse
def publisherWithMostTopHundred(filename):
    with open(filename) as f:
        PublishersTopHundred = {}
        allSales = []
        minTopHundred = 0
        
        reader = csv.reader(f)
        
        for row in reader:
            if(row[6] == "NA_Sales"):
                pass
            else:
                allSales.append(float(row[10]))
        
        allSales.sort()
        minTopHundred = allSales[-100]
        
        f.seek(0) # iterer 2 gange
        
        for row in reader:
            if(row[6] == "NA_Sales"):
                pass
            else:
                PublishersTopHundred.setdefault(row[5], 0)
                if(float(row[10]) >= minTopHundred):
                    PublishersTopHundred[row[5]] += 1         
        #PublisherMostTopHundred = str(max(PublishersTopHundred, key=PublishersTopHundred.get))
        #return PublisherMostTopHundred
        
    top_list = {}
    #Return the top 6 elements in our list. nlargest takes n = elements, iterable = Publishers and opt key which we need here 
    list_of_pub_names = heapq.nlargest(6, PublishersTopHundred, key=PublishersTopHundred.get) 
    for pub in list_of_pub_names:
        top_list[pub] = PublishersTopHundred.get(pub)
    return top_list
       
def plot_most_pop_platform_by_regions(platforms, sales):
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  # explode 1st slice
    plt.title("% of total sales a platform is responsible for in JP, NA and EU", fontsize=16, color="green")
    plt.pie(sales, explode=explode, labels=platforms, colors=colors, autopct='%0.7f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
    
def plot_sum_of_all(countries, bigSum):
    sizes = [215, 130, 245, 210]
    colors = ['yellow', 'red', 'blue', 'green']
    explode = (0.1, 0, 0, 0)  # explode 1st slice
    plt.title("% of how much of global sales a region covers", fontsize=16, color="green")
    plt.pie(bigSum, explode=explode, labels=countries, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
    
def plot_genres2012(tt_labels, tt_values):
    plt.bar(range(len(tt_values)), tt_values, width=0.5, linewidth=0, align='center')
    plt.xticks(range(len(tt_values)), tt_labels, size='small')
    title = 'No. of sales by genre'
    plt.title(title, fontsize=20)
    plt.xlabel("Game genre", fontsize=12)
    plt.ylabel("Sales in millions", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
    
def plot_top_publishers(tt_labels, tt_values):
    plt.bar(range(len(tt_values)), tt_values, width=0.5, linewidth=0, align='center')
    plt.xticks(range(len(tt_values)), tt_labels, size='small')
    title = 'Publishers with most released games in a top 100'
    plt.title(title, fontsize=20)
    plt.xlabel("Publisher", fontsize=12)
    plt.ylabel("No. of games in top 100", fontsize=12)
    plt.tick_params(axis='x', which='major', labelsize=5)
    plt.show()

#Patrick
#platforms = list(find_most_pop_platform_by_regions(filename).keys())
#sales =  list(find_most_pop_platform_by_regions(filename).values())
#plot_most_pop_platform_by_regions(platforms, sales)

#Michael
#countries = list(find_sum_of_all(filename).keys())
#bigSum = list(find_sum_of_all(filename).values())
#plot_sum_of_all(countries, bigSum)

#Martin
#tt_labels = list( genres2012(filename).keys() )
#tt_values = list( genres2012(filename).values() )
#plot_genres2012(tt_labels, tt_values)

#Lasse
#tp_labels = list(publisherWithMostTopHundred(filename).keys())
#tp_values = list(publisherWithMostTopHundred(filename).values())
#plot_top_publishers(tp_labels, tp_values)