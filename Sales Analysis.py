#!/usr/bin/env python
# coding: utf-8

# In[63]:


# Laibraries Importation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import plotly.express as px
sns.set_style("whitegrid")


# In[2]:


# Reading the Dataset
Path = "power bi.xlsx"
df = pd.read_excel(Path , sheet_name = "Data")


# # EDA Which Stands for Exploratory Data Analysis

# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


# Checking for Null or Missing Values inside of our Dataset
df.isna().sum()


# In[7]:


# Investigating if We have Null Values
df.isnull().sum()


# In[8]:


# Duplication Detection
print(df.duplicated().sum())
print("===============================================")
print("we need to Validate the Duplicates in our Dataset & Take the Corrective Actions")


# In[9]:


df.dtypes


# In[10]:


df.columns


# In[11]:


df.head()


# In[12]:


## Performing Uni-Variate Analysis
print(df["Year"].value_counts())
print("===============================================")
print("We've large Sales Transactions in 2019 More than 2020, this indicates that our sales figures has decreased in 2020")


# In[13]:


df["Year"].unique()


# In[14]:


df["Year"].nunique()


# In[15]:


# Defining a Function to Automate Process & Time-Keeping

def getdata(df , Column ):
    
    First = df[Column].unique()
    Socend = df[Column].nunique()
    Third = df[Column].value_counts()
    print(First)
    print("===============================================")
    print(Socend)
    print("===============================================")
    print(Third)
    print("===============================================")
    plt.figure(figsize = (10 , 5))
    print(Third.plot.bar())
    plt.xlabel(Column)
    plt.ylabel("\nFrequency\n")
    plt.legend()
    plt.xticks(rotation = 0.25)
    plt.title("\nFrequency of " + Column + "\n")
    plt.grid(axis = "y" , alpha = 0.7)
    plt.grid( axis = "x" , alpha = 0.7)
    plt.show()


# In[16]:


getdata(df , "Year")
print("===============================================")
print("We've large Sales Transactions in 2019 More than 2020, this indicates that our sales figures has decreased in 2020")


# In[17]:


getdata(df , "Q")
print("===============================================")
print("I've Noticed that Q-4 has Generated the Highest Number of Sales Orders, This May Refer to Seasonality")


# In[18]:


getdata(df , "Month")
print("===============================================")
print("Nov & Oct Has Made the largest Transactions but Dec has the lowest, then Nov & Oct Greatly Contribute to the Overall Sales")


# In[19]:


getdata( df , "Branch")
print("===============================================")
print("Class A has the gratest Contribution to Our Overall Sales, Indicating the it's our Core Target")


# In[20]:


getdata(df , "Product Category")
print("===============================================")
print("We've Earned most Transaction through Electronics Category, Because we'e in the Digitalization World")


# In[21]:


getdata( df , "Product Sub Category")


# In[22]:


# Extracting Some Critical Statistical Insights
df.describe().round().T


# In[23]:


# Statistical Calculations, It Privides the Previous Results but Using another Approach
print(df["Sales"].sum())
print("===============================================")
print(df["Sales"].mean())
print("===============================================")
print(df["Sales"].median())
print("===============================================")
print(df["Sales"].quantile(0.25))
print("===============================================")
print(df["Sales"].quantile(0.05))
print("===============================================")
print(df["Sales"].quantile(0.75))
print("===============================================")
print(df["Sales"].std())


# In[24]:


df.info()


# In[25]:


# Converting Year Datatype From Int into Object
df["Year"] = df["Year"].astype(object)


# In[26]:


# Transforming Datatypes of COGS & Total Cogs to Int
df["COGS per unit"] = df["COGS per unit"].astype(object)


# In[27]:


# Transforming Datatypes of COGS & Total Cogs to Int
df["COGS per unit"] = df["COGS per unit"].astype(int)
df["Total Cogs"] = df["Total Cogs"].astype(int)


# In[28]:


# Checking for Columns Datatypes
df.info()


# In[29]:


# Renaming the Column of COGS per Unit to Cost Per Unit
df.rename(columns = {"COGS per unit" : "Cost Per Unit"} , inplace = True)


# In[30]:


# Renaming the Column of Qty to Sales Volume
df.rename(columns = {"Qty" : "Sales Volume"} , inplace = True)


# In[31]:


# Renaming the Column of Product Category to Category
df.rename(columns = {"Product Category" : "Category"} , inplace = True)


# In[32]:


# Renaming the Column of Product Sub Category to Sub-Category
df.rename( columns = {"Product Sub Category" : "Sub-Category"} , inplace = True)


# In[33]:


# Data Validation After New Adjustments
df.head()


# In[34]:


# Conducting Bi-Variate Analysis
print(df.groupby(['Year'])["Sales"].sum())
print("===============================================")
print(df.groupby(['Year'])["Sales"].sum().plot(kind = 'bar'))
plt.show()


# In[35]:


# Defining a Function to Calculate Valuable Business Insights
def getnumdata(df , Text , INT):
    
    First = df.groupby([Text])[INT].sum().sort_values( ascending = False)
    Socend = df.pivot_table( index = Text , values = INT , aggfunc = "sum")
    print(First)
    print("===============================================")
    print(Socend)
    print("===============================================")
    plt.figure(figsize = (10 , 5))
    print(First.plot.bar(color = 'r'))
    plt.title("\n" + INT + " By " + Text + "\n")
    plt.xlabel(Text)
    plt.ylabel(INT)
    plt.xticks(rotation = 0.25)
    plt.grid(axis = 'y' , alpha = 0.7)
    plt.grid(axis = 'x' , alpha = 0.7)
    plt.show()


# In[36]:


getnumdata(df , "Year" , "Sales")


# In[37]:


getnumdata(df , "Q" , "Sales")


# In[41]:


# Performing Time Serias Analysis
def timeserias(df , Period , Insights):
    
    First = df.groupby([Period])[Insights].sum()
    print(First)
    print("===============================================")
    plt.figure(figsize = (10 , 4))
    print(First.plot( x = First.index , y = First.values , marker = "o" , linestyle = "--" , color = 'blue' , linewidth = 2 ,
                    markersize = 6))
    plt.title("\n " + Insights + " by " + Period + "\n" , fontsize = 14 , fontweight = 'bold' , color = 'darkblue' )
    plt.xlabel("\n" + Period + "\n" , fontsize = 12)
    plt.ylabel("\n" + Insights + "\n")
    plt.legend()
    
    plt.xticks( rotation = 0.25 , fontsize = 12)
    plt.yticks(fontsize = 12)
    
    plt.grid(axis = 'y' , linestyle = '--' , alpha = 0.7)
    
    plt.show()


# In[42]:


timeserias(df , 'Month' , 'Sales')


# In[43]:


timeserias(df , 'Q' , 'Sales')


# In[44]:


timeserias(df , "Year" , "Sales")


# In[47]:


plt.figure( figsize = (10 , 5) )
sns.lineplot( x = "Month" , y = "Sales" , data = df , markers = "o" , color = 'green' , linewidth = 2.5)

plt.title("\nSales By Month\n" , fontsize = 14 , fontweight = 'bold' , color = 'darkblue')
plt.xlabel("\nMonths\n" , fontsize = 10)
plt.ylabel("\nRevenues\n" , fontsize = 10)

plt.legend()

plt.grid(axis = 'y' , linestyle = '--' , alpha = 0.7)

plt.show()


# In[48]:


# Generating a Function for Normal Columns

def linefornormal(df , String , Number):
    
    
    plt.figure( figsize = (10 , 5) )
    sns.lineplot( x = String , y = Number , data = df , markers = "o" , color = 'green' , linewidth = 2.5)

    plt.title("\nSales By Month\n" , fontsize = 14 , fontweight = 'bold' , color = 'darkblue')
    plt.xlabel("\nMonths\n" , fontsize = 10)
    plt.ylabel("\nRevenues\n" , fontsize = 10)

    plt.legend()

    plt.grid(axis = 'y' , linestyle = '--' , alpha = 0.7)

    plt.show()
    
    


# In[49]:


linefornormal(df , "Countries" , 'Total Cogs')


# In[50]:


# Executing Multi-Variate Analysis
df.head()


# In[59]:


# Displaying the Revenues in terms of Countries & Months
df.pivot_table( index = "Countries" , columns = "Month" , values = "Sales" , aggfunc = "sum")


# In[60]:


# Presenting Total Sales by Counrtries & Years

df.pivot_table( index = "Countries" , values = "Sales" , columns = "Year" , aggfunc = "sum")


# In[62]:


# Presenting Total Sales by Counrtries & Quarters

print(df.pivot_table( index = "Countries" , values = "Sales" , columns = "Q" , aggfunc = "sum"))

print("===============================================")

print("Through initial Analysis on our Dataset, we've noticed that in Australia & USA We have on Revenues in Q-4")


# In[68]:


# Ploting a Pie Chart to Demonestrate Sales by Quarter

fig = px.pie( data_frame = df , names = "Q" , values = "Sales" , title = "Sales by Quarter" , color_discrete_sequence = px.colors.qualitative.Set3)
fig.show()


# In[88]:


# Creating a Chart that Showcases our Sales by County

Salesbycountry = df.groupby(['Month'] , as_index = False)['Sales'].sum().sort_values( by = "Sales" , ascending = False)
Salesbycountry = pd.DataFrame(Salesbycountry)


# In[89]:


Salesbycountry.head()


# In[90]:


fig =px.bar(  Salesbycountry , x = "Month" , y = "Sales", title = "Sales by Country" , text = "Sales")
fig.show()


# In[96]:


fig =px.bar(  Salesbycountry , x = "Month" , y = "Sales", title = "Sales by Country" , text = "Sales" , color_continuous_scale = "blues")
fig.update_traces( textposition="outside")
fig.show()


# In[92]:


# Ploting Sales by Country

Sales_country = df.groupby(["Countries"] , as_index = False)["Sales"].sum().sort_values( by = "Sales" , ascending = False)
px.bar( data_frame = Sales_country , x = "Countries" , y = "Sales" , text = 'Sales' , title = "Sales by Country")


# In[97]:


df.head()


# In[130]:


# Most Significant KPIs Extracted From our Business
print("\n=====================KPIs======================\n")
print(f'Our Total Sales : {np.sum(df["Sales"])}')
print("\n===============================================\n")
print(f'Our Avg Sales : {round(np.mean(df["Sales"]) , 2)}')
print("\n===============================================\n")
print(f'Our Total COGS : {np.sum(df["Total Cogs"])}')
print("\n===============================================\n")
print(f'Our Avg Unit Price : {round(df["Unit Price"].mean() , 2)}')
print("\n===============================================\n")
print(f'Our Sales Volume : {np.sum(df["Sales Volume"])}')
print("\n===============================================\n")
print(f'Number of SKUs : {df["Brand"].nunique()}')
print("\n===============================================\n")
print(f'Number of Transations : {df["Year"].count()}')
print("\n===============================================\n")
print(f'Our Unique SBUs : {len(set(df["Brand"]))}')
print("\n===============================================\n")
print(f'Number of Categories : {len(set(df["Category"]))}')
print("\n===============================================\n")
print(f'Number of Sub-Category : {len(set(df["Sub-Category"]))}')
print("\n===============================================\n")
print(f'Number of Branches : {df["Branch"].nunique()}')
print("\n===============================================\n")
print(f'Number of Countries : {len(set(df["Countries"]))}')


# In[ ]:




