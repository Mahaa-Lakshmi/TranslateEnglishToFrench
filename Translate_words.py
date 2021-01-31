import csv
import re
import pandas as pd
import time
import tracemalloc
list3=[[],[],[]]
#To write the performance into performance.txt file
def writePerfomance(start):
    f=open("Performance.txt","w")
    f.write("Time to process:" + str(time.time() - start) + " " + "seconds")
    f.write("Memory used: "+'{:,.0f}'.format(tracemalloc.get_tracemalloc_memory() / float(1 << 20)) + " MB"+"\n")
#The english words are replaced with french words
def change():
    reader = csv.reader(open('french_dictionary.csv', 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v
    fin = open("t8.shakespeare.translated.txt", "wt")
    with open("t8.shakespeare.txt") as f:
        start_time = time.time()
        tracemalloc.start()
        for line in f:
            list2=[]
            for words in line.split():
                if str("".join(re.findall("[a-zA-Z]+", words))) in d.keys():
                    list2.append(d[str("".join(re.findall("[a-zA-Z]+", words)))])
                    list3[0].append(str("".join(re.findall("[a-zA-Z]+", words))))
                    list3[1].append(d[str("".join(re.findall("[a-zA-Z]+", words)))])
                    list3[2].append(0)
                else:
                    list2.append(words)
            fin.write(" ".join(list2))
    print(sorted(list(set(list3[0]))))
    print("Memory used: ", '{:,.0f}'.format(tracemalloc.get_tracemalloc_memory() / float(1 << 20)) + " MB")
    print("Time to process:", time.time() - start_time, "seconds")
    print("Translation done!")
    writePerfomance(start_time)
change()
df = pd.DataFrame({'Eng': list3[0], 'French': list3[1],'Frequency':list3[2]})
df=(df.groupby(['Eng','French'])['Frequency'].count()).drop_duplicates()
df.to_csv('frequency.csv') #Writing to frequency.csv file







