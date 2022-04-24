#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt

path = "/Users/charles/Desktop/18738-myoware-sensor-data/03-31-demo-dataset/all-apply-force.csv"
csv_file = csv.reader(open(path))
data_list = list(csv_file)
row_num = len(data_list)

x = list()
y = list()

for i in range(0, row_num):
    x.append(data_list[i][0])
    y.append(data_list[i][1])

plt.plot(x, y)
plt.show()