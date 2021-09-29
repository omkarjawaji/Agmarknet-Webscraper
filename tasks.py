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


main_url = ""
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(main_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

final_data = pd.DataFrame()

while True:
    try:
        pageSource = driver.page_source
        soup2 = BeautifulSoup(pageSource, 'html.parser')
        table = soup2.find('table', attrs={'class': 'tableagmark_new'})
        aspcalls = table.findAll('input')
        
        tab = driver.find_element_by_id('cphBody_GridPriceData').get_attribute('outerHTML')
        data = pd.read_html(str(tab))[0]
        data.set_index('Sl no.', inplace=True)
        data.dropna(axis=0, inplace=True)
        final_data = pd.concat([final_data, data], axis=0)
        for i in range(len(aspcalls)):
            if (re.sub("[\"\']", "", str(aspcalls[i])).find("Page$Next")):
                next_btn_pos = i
            else:
                break
        element = driver.find_element_by_xpath("//*[@id='cphBody_GridPriceData']/tbody/tr[52]/td/table/tbody/tr/td["+str(next_btn_pos)+"]/input")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(15)
    except:
        print(final_data.shape)
        print(final_data)
        print('break')
        driver.close()
        driver.quit()
        break


hostname = "localhost"
dbname = "ASSIGNMENT"
uname = "tester"
pwd = "1234"

mydb = mysql.connector.connect(host = hostname, user = uname, passwd = pwd)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE ASSGINMENT")

mydbtable = mysql.connector.connect(host = "localhost", user = "tester", passwd = "1234", database= "ASSGINMENT")


sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

final_data.to_sql('task_1', sqlEngine, index=True)
