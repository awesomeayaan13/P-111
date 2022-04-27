import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["ReadingTime"],show_hist=False)
fig.show()
mean=statistics.mean(data)
std_dev=statistics.stdev(data)
print(mean)
print(std_dev)
def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)

    mean=statistics.mean(dataSet)
    stdev=statistics.stdev(dataSet)
   # print(mean)
   # print(stdev)
    return mean


mean_list=[]
for i in range(0,1000):
    setOfMeans=random_set_of_mean(100)
    mean_list.append(setOfMeans)

std_dev=statistics.stdev(mean_list)
print("standard deviation of sampling distribution",std_dev)

mean=statistics.mean(mean_list)
print("mean of sampling distribution",mean)


firstStdDevStart,firstStdDevEnd=mean-std_dev,mean+std_dev
secondStdDevStart,secondStdDevEnd=mean-(2*std_dev),mean+(2*std_dev)
thirdStdDevStart,thirdStdDevEnd=mean-(3*std_dev),mean+(3*std_dev)

print("std1",firstStdDevStart,firstStdDevEnd)
print("std2",secondStdDevStart,secondStdDevEnd)
print("std3",thirdStdDevStart,thirdStdDevEnd)


fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.25],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[firstStdDevStart,firstStdDevStart],y=[0,0.17],mode="lines",name="std1 Start"))
fig.add_trace(go.Scatter(x=[firstStdDevEnd,firstStdDevEnd],y=[0,0.17],mode="lines",name="std1 End"))
fig.add_trace(go.Scatter(x=[secondStdDevStart,secondStdDevStart],y=[0,0.17],mode="lines",name="std2 Start"))
fig.add_trace(go.Scatter(x=[secondStdDevEnd,secondStdDevEnd],y=[0,0.17],mode="lines",name="std2 End"))
fig.add_trace(go.Scatter(x=[thirdStdDevStart,thirdStdDevStart],y=[0,0.17],mode="lines",name="std3 Start"))
fig.add_trace(go.Scatter(x=[thirdStdDevEnd,thirdStdDevEnd],y=[0,0.17],mode="lines",name="std3 End"))
fig.show()
