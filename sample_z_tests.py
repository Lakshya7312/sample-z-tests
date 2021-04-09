import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

dataFrame = pd.read_csv("medium_data.csv")
data = dataFrame["reading_time"].tolist()

population_mean = statistics.mean(data)

def takeSamples(rand):
    dataSet = []

    for i in range(0, rand):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

def setup():
    meanList = []

    for i in range(0, 100):
        setOfMeans = takeSamples(30)
        meanList.append(setOfMeans)

    sampleMean = statistics.mean(meanList)


meanList = []

for i in range(0, 100):
    setOfMean = takeSamples(30)
    meanList.append(setOfMean)

stdevi = statistics.stdev(meanList)
meanMean = statistics.mean(meanList)


firststddevstart, firststddevend = meanMean - stdevi, meanMean + stdevi

secondstddevstart, secondstddevend = meanMean - (2 * stdevi), meanMean + (2 * stdevi)

thirdstddevstart, thirdstddevend = meanMean - (3 * stdevi), meanMean + (3 * stdevi)

zscore1 = (meanMean - population_mean) / stdevi
print(zscore1)

graph = ff.create_distplot([meanList], ["Reading Time"], show_hist=False)
graph.add_trace(go.Scatter(x=[meanList, meanList], y=[0, 0.8], mode="lines", name="Mean List"))
graph.add_trace(go.Scatter(x=[firststddevstart, firststddevstart], y=[0, 0.8], mode="lines", name="Standard Deviation 1 start"))
graph.add_trace(go.Scatter(x=[firststddevend, firststddevend], y=[0, 0.8], mode="lines", name="Standard Deviation 1 end"))
graph.add_trace(go.Scatter(x=[secondstddevstart, secondstddevstart], y=[0, 0.8], mode="lines", name="Standard Deviation 2 start"))
graph.add_trace(go.Scatter(x=[secondstddevend, secondstddevend], y=[0, 0.8], mode="lines", name="Standard Deviation 2 end"))
graph.add_trace(go.Scatter(x=[thirdstddevstart, thirdstddevstart], y=[0, 0.8], mode="lines", name="Standard Deviation 3 start"))
graph.add_trace(go.Scatter(x=[thirdstddevend, thirdstddevend], y=[0, 0.8], mode="lines", name="Standard Deviation 3 end"))
graph.show()