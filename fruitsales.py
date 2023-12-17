import csv

filename = "fruit.csv"

with open(filename, "w", newline="") as csvfile:
  writer = csv.writer(csvfile, dialect="excel")

  writer.writerow(["", "Apples", "Bananas"])
  writer.writerow(["2017 Sales", "35", "21"])
  writer.writerow(["2018 Sales", "41", "34"])