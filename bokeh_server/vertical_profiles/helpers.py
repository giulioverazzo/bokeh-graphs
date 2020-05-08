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
  tot = []
  for line in reader:
      if(line['data']+","+line['ora'] == '2020-01-15,16:30:00'):
        print(line)
      tot.append(line['temp_33m'])
      tot.append(line['temp_10m'])
      tot.append(line['temp_5m'])
      tot.append(line['temp_2m'])

  return min(tot), max(tot)

def get_datetime_string(line):
  if(line != None):
    return f'<ul><li>Date: {line["data"]}</li><li>Time: {line["ora"]}</li></ul>'

#read_csv('data/202001.temp.csv')