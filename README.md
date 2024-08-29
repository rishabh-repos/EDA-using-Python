Zomato Dataset Exploratory Data Analysis

This repository contains a comprehensive Exploratory Data Analysis (EDA) of the Zomato dataset. The analysis explores various aspects of the dataset, such as missing values, numerical and categorical variables, and relationships between features, with visualizations provided using matplotlib and seaborn.


Introduction

The Zomato dataset provides detailed information about restaurants across various countries, including ratings, cuisine types, and delivery options. This project aims to analyze the dataset to uncover trends and insights related to customer ratings, country-specific details, and other significant patterns.

Dataset

The analysis utilizes two datasets:

Zomato.csv: Contains details about restaurants, including ratings, cuisines, and delivery options.
Country-Code.xlsx: Provides a mapping between country codes and country names.

Exploratory Data Analysis

Loading and Overview of Data

Libraries Used: pandas, numpy, matplotlib, seaborn

Initial Exploration: 

Loaded the datasets and displayed the first few rows to understand the structure and content. 

Inspected the column names, data types, and basic statistics.

Handling Missing Values

Identified missing values in each column.

Visualized missing data using a heatmap to understand its distribution across the dataset.

Numerical and Categorical Features Analysis

Conducted descriptive statistics to analyze numerical features.

Explored categorical features such as the distribution of countries in the dataset, online delivery availability, and rating categories.

Data Merging and Feature Relationships

Merged the two datasets on the Country Code to enrich the data.

Analyzed relationships between features like Aggregate rating, Rating color, and Rating text to draw insights about customer feedback across different countries.


Visualizations

Utilized various visualizations to better understand the data:


Pie Charts: To visualize the distribution of restaurants across top countries and cities.

Bar Plots: To analyze the distribution of ratings and their respective colors.

Count Plots: To show the frequency of different rating colors.

Key Insights


Dominant Presence: Zomato has the most records in India, followed by the United States.

Rating Patterns: Higher ratings (4.5 and above) are relatively rare, whereas most ratings fall between 2.5 to 3.4.

Online Delivery Availability: Predominantly available in India and UAE.

Currency Usage: Each country's preferred currency for transactions is identified.
