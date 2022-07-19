# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:20:53 2022

@author: Patri
"""

import pandas as pd
import numpy
import nltk
import string
import collections
#Get stopwords from nltk package
nltk.download('stopwords')
from nltk.corpus import stopwords
import csv
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("N:\\Uni_Bigdata\\titanic.csv")

#Some functions to get info about our data
titanic.head()

titanic.dtypes

titanic.Pclass.unique()

titanic.isna().sum()

titanic.describe()

#Create column family size, which is number of siblings + spouse, 
#plus number of parents and child plus the person him/herself 
titanic['family size'] = titanic['SibSp'] + titanic['Parch'] + 1

#Create empty plot
fig, ax = plt.subplots(figsize = (8, 4))
plt.show()

#Part1

#Gender
titanic.groupby('Sex').size().plot(kind = 'bar', color = 'red')
plt.ylabel('number of passangers')
plt.xlabel('gender')
plt.title('Gender barplot')


#Ticketclass (Assuming Pclass is the Ticketclass)
titanic.groupby('Pclass').size().plot(kind = 'bar')
plt.ylabel('number of passangers')
plt.xlabel('Ticketclass')
plt.title('Ticketclass barplot')

#Survived, changed 0 and 1 to yes/no
titanic.groupby('Survived').size().plot(kind = 'bar')
plt.ylabel('number of passangers')
plt.xlabel('Survival',)
plt.title('Survival barplot')
plt.xticks([0,1],['No','Yes'])

#Part2

#Age
#a few NAs here ...

#Age per Ticketclass 

sns.boxplot(data = titanic, x = 'Pclass', y = 'Age', 
            width = 0.3, boxprops = dict(alpha=0.6))

ax.set_xlabel("Ticketclass")
ax.title.set_text('Age/Ticketclass Boxplot')

plt.show()

#Age per Survival

g = sns.boxplot(data = titanic, x = 'Survived', y = 'Age'
            ,width = 0.3, boxprops = dict(alpha=0.6))

ax.set_xlabel("Survival")
ax.set_xticklabels(("No","Yes"))
g.set_xticks([0,1],['No','Yes'])
ax.title.set_text('Age/Survival Boxplot')

plt.show()

#Part3

#Histogram Travel fare

titanic['Fare'].plot(kind = 'hist', title = 'Travel Fare histogram')
plt.xlabel ('Fare')

#Table Travel fare
# Vector to order the table output

titanic['No_Travel_Fare'] = titanic['Fare'].apply(lambda x: x == 0)

titanic.groupby('No_Travel_Fare').size()
#Or with value counts ; reset_index to create a df
titanic['No_Travel_Fare'].value_counts().reset_index() 


#Appearently there were 10 people  from a 'guarantee group', 
#overseeing the titanic's smooth voyage with a free ticket.
#Others were meant to travel with the ship Philadelphia, 
#but due to scheduling problems Philadelphia's voyage was cancelled.


#Part4

titanic['Pclass'].unique()

pd.to_numeric(titanic['Pclass'])
#Histogram family size / Ticketclass

sns.histplot(data=titanic, x='family size',hue='Pclass'
             ,binwidth=1,palette='bright',multiple='stack')
plt.title('Histplot Family Size/Ticketclass')
plt.legend(title='Ticketclass',labels=sorted(titanic['Pclass'].unique()))

#y='Pclass'


#Part5

#Stacked bar charts of survival differing between gender and ticketclass



ax = titanic.groupby(['Sex','Survived']).size().unstack().plot(kind = 'bar', width = 1, stacked = True)


ax = titanic.groupby(['Pclass','Survived']).size().unstack().plot(kind = 'bar', width = 1, stacked = True)


#fig, ax = plt.subplots(1,3, figsize = (15,8))

#ax[0] = titanic[titanic['Pclass'] == 1].groupby(['Sex','Survived']).size().plot(
#    kind = 'bar', title = 'Ticketclass 1',subplots = 3)
#ax[1] = titanic[titanic['Pclass'] == 2].groupby(['Sex','Survived']).size().plot(
#    kind = 'bar', title = 'Ticketclass 2',subplots = 'true')
#ax[2] = titanic[titanic['Pclass'] == 3].groupby(['Sex','Survived']).size().plot(
#    kind = 'bar', title = 'Ticketclass 3',subplots = 'true')

#Part6

#Violin plot Survival over Age / Gender

ax = sns.violinplot(data = titanic, x = 'Sex', y = 'Age', hue = 'Survived')

handles, labels = ax.get_legend_handles_labels()
labels = ["no", "yes"]
plt.legend(handles,labels)
plt.legend(title='Survival')
plt.xlabel('Gender')
plt.title('Violin Plot Survival over Age / Gender')

plt.show()


#Violin plot Survival over Age / Ticket Class

ax = sns.violinplot(data = titanic, x = 'Pclass', y = 'Age', hue = 'Survived')

handles, labels = ax.get_legend_handles_labels()
labels = ["no", "yes"]
plt.legend(handles,labels)
plt.legend(title='Survival')
plt.xlabel('Ticketclass')
plt.title('Violin Plot Survival over Age / Ticketclass')

plt.show()