# Analysis of Utah Air Quality Index
Exploratory analysis of Utah's Air Quality Index. 

# The Data Files
The data was retrieved from EPA.gov using the Daily AQI pre-generated data files. The raw data files can be accessed here: https://aqs.epa.gov/aqsweb/airdata/download_files.html#AQI

The data files are available by year and for this analysis, a separate data file (Daily AQI by CBSA) for the years 1980-2017 were downloaded. 

__Filename Format:__ daily_aqi_by_cbsa_YYYY.zip

__File combining:__ Files were all downloaded to a folder and then combined using awk within a Terminal window

```sh
awk 'FNR==1 && NR>1{next;}{print}' *.csv > aqi.csv
```
The combined file, for all CBSAs, is made available as part of this project.

__Column Headers__
- __CBSA:__ Core Based Statistical Area
- __CBSA Code:__ Core Based Statistical Area Unique Id
- __Date:__ Reporting Date MM/DD/YYYY
- __AQI:__ Air Quality Index measure for the day; numeric range 0-300+
- __Category:__ AQI category label {see Category Labels below}
- __Defining Parameter:__ The pollutant that defined the AQI score
- __Defining Site:__ Unique Id of data collection site
- __Number of Sites Reporting:__ The number od data collection sites, numeric value.

__Category Labels__

|AQI Range|EPA Color Scale|EPA Descriptor|
| ------------- |:-------------:| -----:|-----:|
|0 to 50|Green|Good|
|51 to 100|Yellow|Moderate|
|101 to 150|Orange|Unhealthy for Sensitive Groups|
|151 to 200|Red |Unhealthy|
|201 to 300|Purple|Very Unhealthy|
|Over 300|Black|Hazardous|

### Todos

 - Validate results
 - Research why so many days in the 1980's top at exactly 200
 - Improve data visualization
 - Moar analysis and insights
