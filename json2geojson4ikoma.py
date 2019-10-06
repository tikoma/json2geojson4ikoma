#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import collections as cl
import json


args= sys.argv
print(args[1][:-5])
assert(args[1][-5:] == ".json")

source = open(args[1], 'r') 
t = json.load(source)  


t1 = t["dataset"]

gj = cl.OrderedDict()
gj["type"] = "FeaturesCollection"
features = list()

for x in t1:

  print(x)
  print("\n")
  lon_value = 0
  lat_value = 0
  afeature = cl.OrderedDict()
  properties = cl.OrderedDict()

  for p in x.keys():
    if (p == "Latitude" or p == "緯度") and x[p] != "":
       lat_value = float(x[p]) 
    elif (p == "Longitude" or p == "経度") and x[p] !="":
       lon_value = float(x[p])
    else:
      properties[p] = x[p]

  afeature["type"] = "Feature"
  afeature["properties" ] = properties
  
  geometry = cl.OrderedDict()
  geometry["type"] = "Point"
  geometry["coordinates"] = [lon_value, lat_value]
  afeature["geometry"] = geometry

  print(afeature)

  features.append(afeature)


  
gj["features"] = features

# target = open('./result.geojson', 'w')
target_file_name = args[1][:-5] + ".geojson"
target = open(target_file_name, 'w')
json.dump(gj, target, ensure_ascii=False, indent=4)


