import csv
import matplotlib.pyplot as plt


avgs = []
ops = []
obp = []



with open('data/joey_votto.csv') as datafile:
    reader = csv.DictReader(datafile)
    for row in reader:
        avgVal = row['BA']
        obpVal = row['OBP']
        opsVal = row['OPS']

        if avgVal != 'BA':
            #print val
            avgs.append(avgVal)
        if opsVal != 'OPS':
            ops.append(opsVal)
        if obpVal != 'OBP':
            obp.append(obpVal)

plt.title("Joey Votto Stats")
plt.xlabel("Game No.")

plt.plot(avgs, label='avg')
plt.plot(ops, label='ops')
plt.plot(obp, label='obp')

plt.legend()

plt.show()