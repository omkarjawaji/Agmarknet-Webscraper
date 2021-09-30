import mysql.connector
from sqlalchemy import create_engine

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

from bs4 import BeautifulSoup
from lxml import html
import urllib.request as urllib3
import time
import re

"""
---Taking input from the user for the task to perform---
Task 1 : Fetch prices data for the commodity Tomato sold in all markets of the Pune district, Maharashtra.
Task 2 : Fetch prices data for the commodity Tomato sold in all markets of all districts of Maharashtra.
Task 3 : Fetch prices data for all commodities sold in all markets of all districts of Maharashtra.
"""

task_no = int(input("Which task to perform ?: "))

"""
---URL Manipulation based on the input---
"""

Tx_State="MH"
DateFrom="01-Jan-2021"
DateTo="10-Aug-2021"
Fr_Date="01-Jan-2021"
To_Date="10-Aug-2021"
Tx_Trend="0"
Tx_StateHead="Maharashtra"

if task_no == 1:
    Tx_Commodity="78"
    Tx_District="14"
    Tx_Market='0'
    Tx_CommodityHead="Tomato"
    Tx_DistrictHead="Pune"
    Tx_MarketHead="--Select--"
elif task_no == 2:
    Tx_Commodity="78"
    Tx_District="0"
    Tx_Market='0'
    Tx_CommodityHead="Tomato"
    Tx_DistrictHead="--Select--"
    Tx_MarketHead="--Select--"
elif task_no == 3:
    Tx_Commodity="0"
    Tx_District="0"
    Tx_Market='0'
    Tx_CommodityHead="--Select--"
    Tx_DistrictHead="--Select--"
    Tx_MarketHead="--Select--"
else:
    print("---Invalid task, please input 1/2/3---")
    quit()


url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity="+Tx_Commodity+"&Tx_State="+Tx_State+"&Tx_District="+Tx_District+"&Tx_Market="+Tx_Market+"&DateFrom="+DateFrom+"&DateTo="+DateTo+"&Fr_Date="+Fr_Date+"&To_Date="+To_Date+"&Tx_Trend="+Tx_Trend+"&Tx_CommodityHead="+Tx_CommodityHead+"&Tx_StateHead="+Tx_StateHead+"&Tx_DistrictHead="+Tx_DistrictHead+"&Tx_MarketHead="+Tx_MarketHead

"""
---Initializing an instance for Selenium Web Driver for Chrome---
"""
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

"""
---Creating a master DataFrame which will eventually have all the data as, with every loop the data gets appended---
"""

final_data = pd.DataFrame()

"""
---A loop to replicate the action of pressing next button if a table extends to next page---
"""

while True:
    try:
        table = driver.find_element_by_id('cphBody_GridPriceData').get_attribute('outerHTML')
        data = pd.read_html(str(table))[0]
        data.set_index('Sl no.', inplace=True)
        data.dropna(axis=0, inplace=True)
        final_data = pd.concat([final_data, data], axis=0)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        find_buttons = soup.find('table', attrs={'class': 'tableagmark_new'})
        aspcalls = find_buttons.findAll('input')
        for i in range(len(aspcalls)):
            if (re.sub("[\"\']", "", str(aspcalls[i])).find("Page$Next")):
                next_btn_pos = i
            else:
                break
                print("couldn't find next button")

        element = driver.find_element_by_xpath("//*[@id='cphBody_GridPriceData']/tbody/tr[52]/td/table/tbody/tr/td["+str(next_btn_pos)+"]/input")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(15)
    except:
        print(final_data.shape)
        print(final_data)
        print('Stopping due to end of data')
        driver.close()
        driver.quit()
        break

"""
---MySQL Database connection---
"""
hostname = "localhost"
dbname = "ASSIGNMENT"
uname = "tester"
pwd = "1234"
table_name = "task_"+str(task_no)

"""
---Creation of Database and table with task number as an appendix---
"""
mydbtable = mysql.connector.connect(host = hostname, user = uname, passwd = pwd, database= dbname)
mycursor = mydbtable.cursor()

# mycursor.execute("CREATE DATABASE ASSIGNMENT")

# create_db = '''
# use assignment;

# CREATE TABLE """+table_name+""" (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     sl_no int, 
#     District_Name VARCHAR(255), 
#     Market_Name VARCHAR(255), 
#     commodity VARCHAR(255), 
#     variety VARCHAR(255), 
#     grade VARCHAR(255),
#     Min_Price_per_Quintal int, 
#     Max_Price_per_Quintal int, 
#     Modal_Price_per_Quintal int, 
#     Price_Date VARCHAR(255)
# );
# '''
# mycursor.execute (create_db)

"""
---Using SQLAlchemy as an Object Relational Mapper to map Pandas data into SQL Database table---
"""

sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

final_data.to_sql(table_name, sqlEngine, index=True)

"""
---Modifying the column names to avoid issues with spaces in table column names---
"""

alter_column_names = """
ALTER TABLE """+table_name+"""
RENAME COLUMN `Sl no.` TO sl_no,
RENAME COLUMN `District Name` TO District_Name,
RENAME COLUMN `Market Name` TO Market_Name,
RENAME COLUMN `Min Price (Rs./Quintal)` TO Min_Price_per_Quintal,
RENAME COLUMN `Max Price (Rs./Quintal)` TO Max_Price_per_Quintal,
RENAME COLUMN `Modal Price (Rs./Quintal)` TO Modal_Price_per_Quintal,
RENAME COLUMN `Price Date` TO Price_Date;
"""

mycursor.execute(alter_column_names)

mycursor.close()