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

url = "https://www.agmarknet.gov.in"

comd_list =[]
comd_ids_list = []
comd_dict = {}
string = """--Select--
Ajwan
Amla(Nelli Kai)
Apple
Arhar (Tur/Red Gram)(Whole)
Arhar Dal(Tur Dal)
Bajra(Pearl Millet/Cumbu)
Banana
Beans
Beetroot
Bengal Gram(Gram)(Whole)
Bhindi(Ladies Finger)
Bitter gourd
Black Gram (Urd Beans)(Whole)
Bottle gourd
Brinjal
Cabbage
Carrot
Castor Seed
Cauliflower
Chikoos(Sapota)
Chili Red
Chilly Capsicum
Chow Chow
Coriander(Leaves)
Corriander seed
Cotton
Cow
Cowpea (Lobia/Karamani)
Cucumbar(Kheera)
Drumstick
Elephant Yam (Suran)
Garlic
Ginger(Green)
Goat
Grapes
Green Chilli
Green Gram (Moong)(Whole)
Green Peas
Groundnut
Guar
Guava
Gur(Jaggery)
Jack Fruit
Jamun(Narale Hannu)
Jowar(Sorghum)
Karbuja(Musk Melon)
Kulthi(Horse Gram)
Lentil (Masur)(Whole)
Lime
Linseed
Little gourd (Kundru)
Maize
Mango
Mango (Raw-Ripe)
Marigold(Calcutta)
Mataki
Methi(Leaves)
Mustard
Neem Seed
Onion
Onion Green
Orange
Other Pulses
Ox
Paddy(Dhan)(Common)
Papaya
Peas Wet
Pineapple
Pomegranate
Potato
Pumpkin
Raddish
Rice
Ridge gourd(Tori)
Safflower
Seetafal
Sesamum(Sesame,Gingelly,Til)
She Buffalo
Sheep
Skin And Hide
Snake gourd
Soyabean
Spinach
Sunflower
Sweet Potato
Sweet Pumpkin
Tamarind Fruit
Tamarind Seed
Tender Coconut
Tomato
Turmeric
Water Melon
Wheat"""

list = string.replace("\n",",").split(",")

comm_page = urllib3.urlopen(url)
comm_soup = BeautifulSoup(comm_page, 'html.parser')

#print(soup.findAll('select', attrs={'id': 'ddlCommodity'}))
comm_list = comm_soup.findAll('select', attrs={'name': 'ctl00$ddlCommodity'})
for option in comm_soup.find('select', attrs={'id': 'ddlCommodity'}).find_all('option'):
    try:
        check_num = option['value']
        check_num= int(check_num)
        comd_dict[option['value']] = option.text
        comd_list.append(option.text)
        comd_ids_list.append(option['value'])
    except:
        break
        print("Issue while fetching commodity")

comd_list = [x for x in comd_list if x not in list]
comd_list = [i.replace(" ","+") for i in comd_list]
        
comd_dict = {key:val for key, val in comd_dict.items() if val not in list}
comd_dict = {key:val.replace(" ","+") for key, val in comd_dict.items() if val in comd_list}

final_data = pd.DataFrame()
for comd_id,comd_name in comd_dict.items():
    Tx_Commodity = comd_id
    Tx_CommodityHead = comd_name
    url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity="+Tx_Commodity+"&Tx_State="+Tx_State+"&Tx_District="+Tx_District+"&Tx_Market="+Tx_Market+"&DateFrom="+DateFrom+"&DateTo="+DateTo+"&Fr_Date="+Fr_Date+"&To_Date="+To_Date+"&Tx_Trend="+Tx_Trend+"&Tx_CommodityHead="+Tx_CommodityHead+"&Tx_StateHead="+Tx_StateHead+"&Tx_DistrictHead="+Tx_DistrictHead+"&Tx_MarketHead="+Tx_MarketHead

    print(url)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)


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

hostname = "localhost"
dbname = "ASSIGNMENT"
uname = "tester"
pwd = "1234"
table_name = "task__"+str(task_no)

# mycursor.execute("CREATE DATABASE ASSIGNMENT")

mydbtable = mysql.connector.connect(host = hostname, user = uname, passwd = pwd, database= dbname)
mycursor = mydbtable.cursor()

sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

final_data.to_sql(table_name, sqlEngine, index=True)

alter_names = """
ALTER TABLE """+table_name+"""
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