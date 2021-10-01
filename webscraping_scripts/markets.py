from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.request as urllib3
from lxml import html
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

url = "https://www.agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=0&Tx_State=MH&Tx_District=0&Tx_Market=0&DateFrom=01-Jan-2021&DateTo=10-Aug-2021&Fr_Date=01-Jan-2021&To_Date=10-Aug-2021&Tx_Trend=0&Tx_CommodityHead=--Select--&Tx_StateHead=Maharashtra&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--"

id = 0
dist_data = {}
mark_data = {}
district_names_list = []
district_ids_list = []
market_names_list = []
market_ids_list = []

page = urllib3.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
for option in soup.find('select', attrs={'id': 'ddlDistrict'}).find_all('option'):
    try:
        district_ids_list.append(int(option['value'])) 
        district_names_list.append(option.text)
    except:
        break

row_cnt = [x for x in range(len(district_ids_list))]

dist_data["d_id"] = row_cnt[1:]
dist_data["district_Id"] = district_ids_list[1:]
dist_data["district_Name"] = district_names_list[1:]

dist_tuple = [(district_ids_list[i], district_names_list[i]) for i in range(1, len(district_ids_list))]

final_data = pd.DataFrame()

for id, name in dist_tuple:
    id = str(id)
    name = name.replace(" ","+")
    mark_url = "https://www.agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=0&Tx_State=MH&Tx_District="+id+"&Tx_Market=0&DateFrom=01-Jan-2021&DateTo=10-Aug-2021&Fr_Date=01-Jan-2021&To_Date=10-Aug-2021&Tx_Trend=0&Tx_CommodityHead=--Select--&Tx_StateHead=Maharashtra&Tx_DistrictHead="+name+"&Tx_MarketHead=--Select--"

    page = urllib3.urlopen(mark_url)
    soup = BeautifulSoup(page, 'html.parser')

    for option in soup.find('select', attrs={'id': 'ddlMarket'}).find_all('option'):
        try:
            if int(option['value']) != 0:
                market_ids_list.append(int(option['value'])) 
                market_names_list.append(option.text)
        except:
            break

    row_cnt = [x for x in range(len(market_ids_list))]

    mark_data["district_id"] = id
    mark_data["m_id"] = row_cnt[1:]
    mark_data["market_Id"] = market_ids_list[1:]
    mark_data["market_Name"] = market_names_list[1:]
    df = pd.DataFrame(mark_data)
    df.index += 1

    final_data = pd.concat([final_data, df], axis=0)


print(mark_data)
print(final_data)


hostname = "localhost"
dbname = "options"
uname = "tester"
pwd = "1234"
table_name = "markets"

# mydb = mysql.connector.connect(host = hostname, user = uname, passwd = pwd)
# mycur = mydb.cursor()

# mycur.execute("CREATE DATABASE options")
# mydbtable = mysql.connector.connect(host = hostname, user = uname, passwd = pwd, database= dbname)
# mycursor = mydbtable.cursor()
# create_table = """
# CREATE TABLE """+table_name+""" (
#     c_id INT PRIMARY KEY,
#     Commodity_Id int, 
#     Commodity_Name VARCHAR(255)
# );
# """
# mycursor.execute (create_table)

sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

final_data.to_sql(table_name, sqlEngine, index=False)

# mycur.close()
# mycursor.close()
