# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:30:50 2019

@author: STEM
"""
    
Cadbury1= "Milk Chocolate"

Cadbury2= "Dark Chocolate"

Cadbury3= "White Chocolate"

MilkChocolate=6 

DarkChocolate=5

WhiteChocolate=8

print(WhiteChocolate)

WhiteChocolate

CadburyM= "6 milk chocolate"

CadburyD= "5 dark chocolate"

CadburyW= "8 white chocolate"

cad1="dark"
cad2="milk"
cad3="white"

chocolate1={"CadburyM":5}
chocolate2={"CadburyD":8}
chocolate3={"CadburyW":3}

print (chocolate1)

chocolatebox ={"dark":5,"milk":6,"white":8}
chocolatebox

StudentInfo= {"Steve":32,"Lia":28,"Vin":45, "Katie":38}
StudentInfo

StudentAge= {"Steve":32,"Lia":28,"Vin":45, "Katie":38}
StudentAge

StudentGender={"Steve":"M", "Lia": "F", "Vin" : "M" , "Katie" :"F"}

StudentList=[["Steve", 32, "M"],["Lia", 28, "F"],["Vin", 45, "M"], ["Katie",38,"F"]]
StudentList

student= [StudentAge, StudentGender]
student

import pandas
dir(pandas)

studentdf = pandas.DataFrame(StudentList)
studentdf

studentdf = pandas.DataFrame(StudentList, columns=("name", "age" , "gender"))
studentdf["name"]
studentdf["age"]

Chocolates= [["Dark",8],["White",3],["Milk",5]]

import pandas

dir(pandas)

Chocolatesdf = pandas.DataFrame(Chocolates, columns=("Quantity" , "Type"))
Chocolatesdf["Quantity"]
Chocolatesdf["Type"]

#datafrane of studentinfo

StudentList= [["Steve", 32, "M"],["Lia", 28, "F"],["Vin",45, "M"],["Katie", 38, "F"]]
StudentList

import pandas

Studentdf= pandas.DataFrame (StudentList, columns=("name", "age" , "gender"))
Studentdf

Studentdf2= pandas.DataFrame(StudentList, columns=("1","2","3"))
Studentdf2

Studentdf2= pandas.DataFrame (StudentList, columns = ("name", "age" , "gender"),index=["1","2","3","4"])
Studentdf2

#plotting data

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

StudentBar=go.Bar(x=Studentdf["name"],y=Studentdf["age"])
plot([StudentBar])

ChocolateBar=go.Bar(x=Chocolatesdf["Quantity"],y=Chocolatesdf["Type"])
plot([ChocolateBar])

title = go.Layout(title= "Numer of chocolates by type")

ChocolateBar=go.Bar(x=Chocolatesdf["Chocolate"],y=Chocolatesdf["Type"])

fig = go.Figure(data=[ChocolateBar], layout=titles)
plot(fig)

