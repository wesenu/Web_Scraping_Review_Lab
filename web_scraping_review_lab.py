# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

import requests

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

#import beautifulsoup
from bs4 import BeautifulSoup

soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag
    # Get all columns in each row.cols=row.find_all('td')# in html a column is represented by the tag
    
    cols = row.find_all('td')
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
    
## Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
##################
import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag

# we can see how many tables were found by checking the length of the tables list
len(tables)

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        #population_data = pd.concat({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(population_data)

### Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html

pd.read_html(str(tables[5]), flavor='bs4')

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html

## Scrape data from HTML tables into a DataFrame using read_html

dataframe_list = pd.read_html(url, flavor='bs4')

len(dataframe_list)

print(dataframe_list[5])

pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
























