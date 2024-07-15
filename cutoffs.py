#!/usr/bin/env python3

from csv import reader

table = list(reader(open(input("CSV file to read: "),"r"),delimiter=","))
mydict = {}

def tally(name,score,sgn):
   if name:
      if name not in mydict:
         mydict[name] = {}
         mydict[name][score] = sgn
      elif score not in mydict[name]:
         mydict[name][score] = sgn
      else: mydict[name][score] += sgn

for row in table:
   try:
      score = int(row[1])
      if score in range(-142,427):
         tally(row[2],score,1)
         for name in row[3].split(";"): tally(name,score,-1)
   except: pass

for name in mydict:
   subdict = dict(sorted(mydict[name].items()))
   prev = 0
   value = greatest = sum(subdict.values())
   for score in subdict:
      value -= prev + subdict[score]
      if value >= greatest:
         greatest = value
         cutoff = score
      prev = subdict[score]
   print("Cutoff for " + name + " is " + str(cutoff))
