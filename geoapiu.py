import requests
#from shapely.geometry import Polygon
import json
import sys,os
import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import math
from area import area
import matplotlib.pyplot as plt
import pandas as pd
import csv
import operator


reader=pd.read_csv("States.csv")
df=pd.DataFrame(reader)
staten=df['Name']
abbr=df['State']
dstate={}
for i in range(0,51):
    dstate[staten[i]]=abbr[i]

def segments(poly):
    return zip(poly, poly[1:] + [poly[0]])
url1="https://nominatim.openstreetmap.org/search.php?q="
url2=sys.argv[1]
urlextr="+"
url3=sys.argv[2]
url4="&polygon_geojson=1&format=json"
url2=url2.title()
if(url3=='usa' or url3=='us' or url3=='America' or url3=='United States of America'):
    gstate=dstate[url2]

URL=url1+url2+urlextr+url3+url4
r=requests.get(url= URL)
data=r.json()
#print(data)
i=0
for i in range(0,len(data)):
    if(data[i]['geojson']['type']=='Polygon'):
        a1=data[i]
        break
print('Name of the district:' + data[i]['display_name'])
imp=str(data[i]['importance'])
print('Administrative importance of the the district is:' + imp)
imp=float(imp)
#imp=math.sqrt(imp+0.5)
a2=a1['geojson']
a=area(a2)
a=math.sqrt(a)
a=a/100000
a=a*a
area=a
a=str(a)
print('Area of the specified place is:'+ a)
#print(a)
a3=a2['coordinates']
a4=a3[0]
p=abs(sum(math.hypot(x0-x1,y0-y1) for ((x0, y0), (x1, y1)) in segments(a4)))
#p=p*100000
#p=Polygon(a4).length
peri=p
p=str(p)
print('Perimeter of the specified place is:' + p)
#print(p)
comp=((4*3.14159)*area)/(peri*peri)
r=imp/comp
r=str(r)
comp=str(comp)
print('Compactness using polsby poppers is:' + comp)
print('Ratio:'+r)
comp=float(comp)
listy=a4
x=[]
y=[]
fig= plt.subplots()
for z in range(0,len(listy)):
    temp=listy[z][0]
    x.append(temp)
    temp2=listy[z][1]
    y.append(temp2)
plt.plot(x,y)
plt.title('Boundaries of: '+ data[0]['display_name'])
#plt.show()
mu = 0.5
variance = 0.035
sigma = math.sqrt(variance)
fig1= plt.subplots()
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,norm.pdf(x, mu, sigma))
plt.axvline(x=comp,color='r')
plt.title('Compactness shown on a Normal distribution curve')
#plt.show()
fig3= plt.subplots()
mu = 0.5
variance = 0.035
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,norm.pdf(x, mu, sigma))
compy=1-comp
prob=((14*compy)+(1*imp))/15
#prob=(compy*imp)
#if(prob>0.5):
#    prob=prob*1.25
#else:
#    prob=prob*0.8
plt.axvline(x=prob,color='r')
plt.title('Probablity of gerrymandering shown on a Normal distribution curve')
#plt.show()
url2=url2.title()
if(url3=='usa' or url3=='us' or url3=='America' or url3=='United States of America'):
    gstate=dstate[url2]
reader1=pd.read_csv("EnPvotes.csv")
df1=pd.DataFrame(reader1)
c=-1
for i in abbr:
    c=c+1
    if(i==gstate):
        index=c
plt.rcdefaults()

fig, ax = plt.subplots()
r2=pd.read_csv("Candidates.csv")
df2=pd.DataFrame(r2)
l4=df2.loc[index]
dlist4=list(l4[1:4])
#fig4,ax4 = plt.subplots()
labels4='Republicans','Democrats','Others'
sizes4=dlist4
ax.pie(sizes4, labels=labels4, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Candidates voting per party')


r=pd.read_csv("EnPvotes.csv")
df1=pd.DataFrame(r)
l=df1.loc[index]
l.fillna(0, inplace = True) 
dlist=list(l[1:6])
print(dlist)
fig2, (ax2, ax3) = plt.subplots(nrows=2, ncols=1)
labels='Republicans','Democrats'
sizes1=dlist[0:2]
ax2.pie(sizes1, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax2.axis('equal')
ax2.set_title('Electoral votes for the state')# Equal aspect ratio ensures that pie is drawn as a circle.
labels2='Republicans','Democrats','Others'
sizes2=dlist[2:5]
ax3.pie(sizes2, labels=labels2, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal')
ax3.set_title('Popular votes for the state')
plt.show()
#scaling
#descision tree
if(imp>0.8):
        #low probability area
        #check importance
        if(comp<=0.4):
                print("Probability of gerrymandering "+url2+" is HIGH")
        elif(comp>0.4 and comp<=0.8):
                print("Probability of gerrymandering "+url2+" is MEDIUM")
        elif(comp>0.8):
                 print("Probability of gerrymandering "+url2+" is LOW")

if(imp>0.4 and imp<=0.8):
        if(comp<=0.4):
                print("Probability of gerrymandering "+url2+" is HIGH")
        elif(comp>0.4 and comp<=0.8):
                print("Probability of gerrymandering "+url2+" is MEDIUM")
        else:
                print("Probability of gerrymandering "+url2+" is LOW")
if(imp<=0.4):
        if(comp<=0.4 or (comp>0.4 and comp<=0.8)):
                print(print("Probability of gerrymandering "+url2+" is MEDIUM"))
        elif(comp>0.8):
                print("Probability of gerrymandering "+url2+" is LOW")


        


