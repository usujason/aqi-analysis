
# coding: utf-8

# # Analysis of Utah Air Quality Index
# Exploratory analysis of Utah's Air Quality Index. 
# 
# # The Data Files
# The data was retrieved from EPA.gov using the Daily AQI pre-generated data files. The raw data files can be accessed here: https://aqs.epa.gov/aqsweb/airdata/download_files.html#AQI
# 
# The data files are available by year and for this analysis, a separate data file (Daily AQI by CBSA) for the years 1980-2017 were downloaded. 
# 
# __Filename Format:__ daily_aqi_by_cbsa_YYYY.zip
# 
# __File combining:__ Files were all downloaded to a folder and then combined using awk within a Terminal window
# 
# ```sh
# awk 'FNR==1 && NR>1{next;}{print}' *.csv > aqi.csv
# ```
# The combined file, for all CBSAs, is made available as part of this project.
# 
# __Column Headers__
# - __CBSA:__ Core Based Statistical Area
# - __CBSA Code:__ Core Based Statistical Area Unique Id
# - __Date:__ Reporting Date MM/DD/YYYY
# - __AQI:__ Air Quality Index measure for the day; numeric range 0-300+
# - __Category:__ AQI category label {see Category Labels below}
# - __Defining Parameter:__ The pollutant that defined the AQI score
# - __Defining Site:__ Unique Id of data collection site
# - __Number of Sites Reporting:__ The number od data collection sites, numeric value.
# 
# __Category Labels__
# 
# |AQI Range|EPA Color Scale|EPA Descriptor|
# |--|-------------------------------|------------|-------------|
# |0 to 50|Green|Good|
# |51 to 100|Yellow|Moderate|
# |101 to 150|Orange|Unhealthy for Sensitive Groups|
# |151 to 200|Red |Unhealthy|
# |201 to 300|Purple|Very Unhealthy|
# |Over 300|Black|Hazardous|
# 
# ### Todos
# 
#  - Validate results
#  - Research why so many days in the 1980's top at exactly 200
#  - Improve data visualization
#  - Moar analysis and insights
# 
# 
# 
# 

# In[2]:

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime

get_ipython().magic(u'matplotlib inline')


# In[3]:

#import daily AQI data for all CBSAs
aqi_all = pd.read_csv('https://www.33sticks.com/projects/python/aqi/daily_aqi.csv', parse_dates=["Date"])


# In[4]:

#examine the file contents
aqi_all.head()


# In[5]:

#try to locate only utah CBSA entries
aqi_all[aqi_all['CBSA'].str.contains(", UT")]


# In[6]:

#create a Utah only dataframe
aqi_ut = aqi_all[aqi_all['CBSA'].str.contains(", UT")]


# In[7]:

#exaine the Utah only dataframe
aqi_ut.head(n=5)


# In[17]:

#create a new column to easily group daily entries by year
aqi_ut['Year'] = aqi_ut['Date'].dt.year


# In[18]:

#examine the data types associated with the Utah dataframe
aqi_ut.dtypes


# In[19]:

#generate summary statstic for the Utah dataframe
aqi_ut.describe()


# In[20]:

#list all of the CBSAs located within the Utah dataframe
aqi_ut.CBSA.unique()


# In[21]:

#create an SLC dataframe to focus investigation on Salt Lake City
aqi_slc = aqi_ut[aqi_ut['CBSA'].str.contains("Salt Lake City, UT")]


# In[22]:

#create a simple daily8 plot to observe distribution of data
plt.figure(figsize=(50,20))
plt.ylim(0, 250)
plt.ylabel('Air Quality Index (AQI)')
plt.xlabel('Year')
plt.title('AQI for Salt Lake City Metro by Day')
plt.plot(aqi_slc.Date, aqi_slc.AQI, marker='o')

#add horizontal markers to indicate change in AQI Category Label
plt.axhline(y=51, linewidth=8, color='#FFFF00')
plt.axhline(y=101, linewidth=8, color='#FFA500')
plt.axhline(y=151, linewidth=8, color='#FF0000')
plt.axhline(y=0, linewidth=18, color='#008000')



# In[24]:

#create a plot to visualize trend of each AQI Category Label over time
fig, ax = plt.subplots(figsize=(15,8))
plt.ylabel('Number of Days')
plt.title('Salt Lake City AQI Category Count by Year')
aqi_slc.groupby(['Year', 'Category']).count()['AQI'].unstack().plot(ax=ax)


# In[25]:

#isolate the impact of ozone as a pollutant 
ozone= aqi_slc[aqi_slc['Defining Parameter'].str.contains("Ozone")]

ozone_year= ozone.groupby(['Year'])
ozone_year.describe()


# In[26]:

#plot the number of day where ozone was the defining pollutant parameter
plt.ylabel('Number of Days')
ozone_year['AQI'].count().plot(figsize=(15,8),title="Salt Lake City Metro - Ozone AQI Days")

