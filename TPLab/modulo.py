import csv
import matplotlib.pyplot as plt

frecs = []
gains = []
frec = []
gain = []

with open('modulo.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    for row in csv_reader:
        line_count += 1
        if line_count > 107 and len(row) > 1:
            frecs.append(row[0])
            gains.append(row[1])
            i += 1
    
for j in range(len(frecs)-1):
    frec.append(float(frecs[j]))
    gain.append(float(gains[j]))

plt.plot(frec,gain)
plt.show()