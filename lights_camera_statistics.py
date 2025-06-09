# Data Preparation and Cleaning

%cd /content/drive/MyDrive/Statistics with Python/Inferential Statistics/Capstone Project - Lights, Camera, Statistics!

# Import libraries
import pandas as pd
import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt

# data
data = pd.read_csv("imdb.csv")
data.head()

# Pick some variables
df = data[['IMDB_Rating', 'Released_Year', 'Runtime',
           'Meta_score', 'Gross', 'Director']]
df.head()

# Look at df
df.info()

# Convert Released_Year to numeric
df['Released_Year'] = pd.to_numeric(df['Released_Year'],
                                    errors='coerce')

# Check Row 966
df.iloc[966]

# Create a decade variable
df['Decade'] = np.floor(df['Released_Year'] / 10) * 10

# Convert and transform Runtime
df['Runtime'] = df['Runtime'].str.replace(" min", "").astype(int)

# Fill NaN values with zero
df["Gross"] = df['Gross'].fillna(0)
print(df['Gross'].isna().sum())

# Convert and transform the Gross Variable
df["Gross"] = df['Gross'].str.replace(',', '').fillna(0).astype(int)

# Creating a mil variable for Gross
df['Gross_mil'] = df['Gross'] / 1000000

df.head()

# Finalize this df
df = df.drop(columns=['Released_Year', 'Gross'], axis=1)
df.head()

# Exploratory Data Analysis

# Summary Statistics
df.describe()

# Histogram of the IMDB ratings
sns.histplot(df['IMDB_Rating'], kde=True)
plt.title('IMDB Rating Distribution')
plt.show()

# Study the top 10 directors with the highest avg IMDB rating
director_ratings = (df.groupby('Director')['IMDB_Rating'].mean().sort_values(ascending=False).head(10))
director_ratings

# Visualize the Mean IMDB ratings for the top 10 directors
plt.figure(figsize=(12, 4))
sns.barplot(x = director_ratings.index,
            y = director_ratings.values)
plt.xticks(rotation=45)
plt.xlabel('Director')
plt.ylabel('IMDB average rating')
plt.show()

# Distribution of IMDB ratings by decade
plt.figure(figsize=(12, 4))
sns.boxplot(x='Decade',
            y='IMDB_Rating',
            data=df)

plt.xticks(rotation=45)
plt.title("IMDB Rating Distribution by Decade")
plt.show()

# Covariance matrix
df_co = df[['Runtime', 'IMDB_Rating', 'Gross_mil', 'Meta_score']]
df_co.cov()

# Correlation heatmap
plt.figure(figsize=(8,4))
sns.heatmap(df_co.corr(),
            annot = True,imdb_
            cmap='coolwarm')
plt.show()

# Calculate the mean, the standard deviation and the sample size
summary = df.groupby('Decade').agg({'Gross_mil': ['mean', 'std', 'count']})

# Rename the columns
summary.columns = ['Gross_mean', 'Gross_std', 'Gross_count']

# Calculate the SEM
summary['Gross_sem'] = summary['Gross_std'] / np.sqrt(summary['Gross_count'])
summary.head()

 # Calculate the confidence interval with 95% CL
alpha = 0.05
summary['tscore'] = st.t.ppf(1-alpha / 2,
         summary['Gross_count'] - 1) # degree of Freedom

# Confidence Interval
summary['lower_ci'] = summary['Gross_mean'] - summary['tscore'] * summary['Gross_sem']
summary['upper_ci'] = summary['Gross_mean'] + summary['tscore'] * summary['Gross_sem']

# Display outcome
summary

# Conclusions

# 1) The average movie duration for highly rated movies is 123 min

# 2) Frank Darabont makes the highest rated movies

# 3) 2020 has the most outliers when it comes to highly rated movies (in a positive way)

# 4) Runtime has a positive relationship with the IMDB rating but no relationship with meta score

# 5) Either people prefer recent movies or recent movies have higher quality

# 6) In the decade of 2020, a highly rated movie is expected to earn above 100M
