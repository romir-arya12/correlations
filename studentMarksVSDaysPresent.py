import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    studentMarks=[]
    daysPresent=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            studentMarks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return {"x":studentMarks,"y":daysPresent}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between student makrs of days present is: ",correlation[0,1])
def setup():
    data_path="./Student Marks vs Days Present.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()