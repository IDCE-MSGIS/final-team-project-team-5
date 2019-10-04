# Name: Brissa Ramos, Mingshuang Lian
# Assignment title: Project Script 1
# Time to complete: 30 min
# Description: Provides the weather forcest of the users chosen location based on latitude and longitude

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
#lat = '42.2634'
#lon = '-71.8022'

#asks user of longitude and latitude
lat = input('Enter latitude: ')
lon = input('Enter longitude: ')

#converts to float input to string by reassigning
lat = str(lat)
lon = str(lon)

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
    #adds space between "chance" and "showers"
    day = day.replace('ChanceShowers', 'Chance Showers')
    #adds space before "Low", "High", and "Night"
    day = day.replace('Low', ' Low')
    day = day.replace('High', ' High')
    day = day.replace('Night', ' Night')
    day = day.replace('then', ' then')
    day = day.replace('Showers','Showers ')
    day = day.replace('Likely','Likely ')
    day = day.replace('This', 'This ')
    #makes output uppercase
    day = day.upper()
    print day
