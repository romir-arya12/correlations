import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    sizeOfTv=[]
    averageTimeSpent=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            averageTimeSpent.append(float(row["Average time spent watching TV in a week"]))
            sizeOfTv.append(float(row["Size of TV"]))
    return {"x":averageTimeSpent,"y":sizeOfTv}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between average time spent of size of tv is: ",correlation[0,1])
def setup():
    data_path="./Size of TV,Average time spent watching TV in a week.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()