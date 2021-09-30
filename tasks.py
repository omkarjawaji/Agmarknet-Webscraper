import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from lxml import html
import urllib.request as urllib3
import time
import re
import mysql.connector
from sqlalchemy import create_engine

task_no = int(input("Which task to perform ?: "))

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


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

final_data = pd.DataFrame()

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
        print('break, last table')
        driver.close()
        driver.quit()
        break


hostname = "localhost"
dbname = "ASSIGNMENT"
uname = "tester"
pwd = "1234"
table_name = "task_"+str(task_no)

# mycursor.execute("CREATE DATABASE ASSIGNMENT")

mydbtable = mysql.connector.connect(host = hostname, user = uname, passwd = pwd, database= dbname)
mycursor = mydbtable.cursor()

sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

final_data.to_sql(table_name, sqlEngine, index=True)

alter_names = """
ALTER TABLE task_"""+str(task_no)+"""
RENAME COLUMN `Sl no.` TO sl_no,
RENAME COLUMN `District Name` TO District_Name,
RENAME COLUMN `Market Name` TO Market_Name,
RENAME COLUMN `Min Price (Rs./Quintal)` TO Min_Price_per_Quintal,
RENAME COLUMN `Max Price (Rs./Quintal)` TO Max_Price_per_Quintal,
RENAME COLUMN `Modal Price (Rs./Quintal)` TO Modal_Price_per_Quintal,
RENAME COLUMN `Price Date` TO Price_Date;
"""

mycursor.execute(alter_names)

mycursor.close()