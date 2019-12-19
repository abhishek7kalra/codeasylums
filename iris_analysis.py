# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:51:21 2019

@author: Abhishek
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Abhishek/Downloads/iris.csv')
sl=df['sepal.length']
sw=df['sepal.width']
pl=df['petal.length']
pw=df['petal.width']

sl.plot.kde()
sw.plot.kde()
pl.plot.kde()
pw.plot.kde()

print(sl.mean() ,"mean of sepal length")
print(df['sepal.width'].mean(),"mean of sepal width")
print(df['petal.length'].mean(),"mean of petal length")
print(df['petal.width'].mean(),"mean of petal width")

print(sl.mode() ,"mode of sepal length")
print(sw.mode(),"mode of sepal width")
print(pl.mode(),"mode of petal length")
print(pw.mode(),"mode of petal width")

print(sl.median() ,"median of sepal length")
print(sw.median(),"median of sepal width")
print(pl.median(),"median of petal length")
print(pw.median(),"median of petal width")

sl_length=len(sl)
sw_length=len(sw)
pl_length=len(pl)
pw_length=len(pw)
if(sl_length==sw_length and pl_length==pw_length and sl_length==pw_length):
    print("balanced dataset")
else:
    print("\n unbalanced dataset")

plt.matshow(df.corr())

print(df.corr())

print("Either petal width or petal length can be dropped out to reduce dimentionality of the data")

