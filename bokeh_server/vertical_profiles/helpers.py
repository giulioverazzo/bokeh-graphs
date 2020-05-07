import csv

''' reads a csv file and returns a csv.DictReader (a reader object that can be iterated).
    Each object is a dict.


def read_csv(filepath, callback):
  with open(filepath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    callback(reader)
'''

def read_csv(filepath):
  with open(filepath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    return list(reader)

def get_min_max(reader):
  tot_min = []
  tot_max = []
  for line in reader:
      tot_min.append(min(line['temp_33m'], line['temp_10m'], line['temp_5m'], line['temp_2m']))
      tot_max.append(max(line['temp_33m'], line['temp_10m'], line['temp_5m'], line['temp_2m']))
  
  return min(tot_min), max(tot_max)

#read_csv('data/202001.temp.csv')