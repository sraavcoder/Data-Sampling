import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import csv
import plotly.graph_objects as go

df = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Data Sampling/Data.csv")

data = df["reading_time"].tolist()

meanForPopulation = statistics.mean(data)
SDForPopulation = statistics.stdev(data)

print("Mean of the Population Is : ", meanForPopulation)
print("Standard Deviation of the Population is : ", SDForPopulation)


def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean


def show_fig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["Reading_Time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[
                  0, 2.5], mode="lines", name="Mean"))
    fig.show()


def setUp():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(300)
        meanList.append(setOfMeans)
    show_fig(meanList)
    mean = statistics.mean(meanList)
    print("Mean of the Sampling Distribution Is : ", mean)


setUp()


def standard_deviation():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(300)
        meanList.append(setOfMeans)
    standardDeviation = statistics.stdev(meanList)
    print("Standard Deviation of the Sampling Distribution is : ", standardDeviation)


standard_deviation()
