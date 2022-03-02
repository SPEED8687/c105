import pandas as pd
import math
df=pd.read_csv('class1.csv')
marks=df['Marks'].tolist()
sum=0
for data in marks :
    sum=sum+data
mean=sum/len(marks)
n=len(marks)
a=0
for data in marks :
    r=data-mean
    s=r*r
    a=a+s
d=a/(n-1)
result=math.sqrt(d)
print(result)