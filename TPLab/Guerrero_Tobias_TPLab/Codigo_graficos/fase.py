import csv
import matplotlib.pyplot as plt

frecs = []
phases = []
frec = []
phase = []

with open('fase.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    for row in csv_reader:
        line_count += 1
        if line_count > 107 and len(row) > 1:
            frecs.append(row[0])
            phases.append(row[1])
            i += 1
    
for j in range(len(frecs)-1):
    frec.append(float(frecs[j]))
    if frec[j] < 5900:
        phase.append(float(phases[j])+360)
    else: 
        phase.append(float(phases[j]))

plt.plot(frec,phase)
plt.show()