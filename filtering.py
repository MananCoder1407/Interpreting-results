import csv
import pandas as pd;

rows = []

with open("gravity_merged_data.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

planet_data_rows = rows[1:]

suitable_planets = [];

for i in planet_data_rows:
    if float(i[2]) <= float(100) and float(i[5]) >= 150 and float(i[5]) <= 350:
        suitable_planets.append(i);

name = [];
distance = [];
mass = [];
radius = [];
gravity = [];

for i in suitable_planets:
  name.append(str(i[1]));
  distance.append(float(i[2]));
  mass.append(float(i[3]));
  radius.append(float(i[4]));
  gravity.append(float(i[5]));

dict = {'name' : name, 'distance' : distance, 'mass' : mass, 'radius' : radius, 'gravity' : gravity};
final_df = pd.DataFrame(dict);

final_df.to_csv('/Users/mananjain/Desktop/Solar Planets Prtc/final_stars.csv');