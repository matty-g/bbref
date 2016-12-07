import csv
import matplotlib.pyplot as plt


def displayAvg(player_data):

    avgs = []

    with open(player_data) as datafile:
        reader = csv.DictReader(datafile)

        for row in reader:
            avg = row['BA']
            if '.' in avg and avg is not None:
                avgs.append(avg)

        plt.title("Joey Votto Stats")
        plt.xlabel("Game No.")
        plt.plot(avgs, label="avg")
        plt.legend()
        plt.show()


def calcAvg(sumTotal, count):
    return float(sumTotal)/count


#displayAvg('data/joey_votto.csv')
displayAvg('data/jay_bruce.csv')
