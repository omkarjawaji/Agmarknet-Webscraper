import pandas as pd
from time import sleep


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

url = 'https://www.agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=MH&Tx_District=14&Tx_Market=172&DateFrom=01-Jan-2021&DateTo=27-Sep-2021&Fr_Date=01-Jan-2021&To_Date=27-Sep-2021&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=Pune'


d = webdriver.Chrome(ChromeDriverManager().install())
d.get(url)
commodity = Select(d.find_element_by_id('ddlCommodity')).options
commodity = [(i.get_attribute('value'), i.text) for i in commodity[1:]]
states = Select(d.find_element_by_id('ddlState')).options
states = [(i.get_attribute('value'), i.text) for i in states[1:]]

print(states)
print(commodity)


for i, j in states:
  if j=='Maharashtra':
    c, d = i, j
    break


final_df = pd.DataFrame()
for a, b in commodity:
    temp_df = pd.DataFrame()
    url = 'https://www.agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity='+a+'&Tx_State='+c+'&Tx_District=0&Tx_Market=0&DateFrom=01-Jan-2021&DateTo=10-Aug-2021&Fr_Date=01-Jan-2021&To_Date=10-Aug-2021&Tx_Trend=0&Tx_CommodityHead='+b+'&Tx_StateHead='+d+'&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--'
    # print(url)
    dr = webdriver.Chrome(ChromeDriverManager().install())
    dr.get(url)

    while True:  
        try:
            table = dr.find_element_by_id('cphBody_GridPriceData').get_attribute('outerHTML')
            data = pd.read_html(str(table))[0]
            data.dropna(axis=0, inplace=True)
            if len(data)>1:
                data.set_index('Sl no.', inplace=True)
                temp_df = pd.concat([temp_df, data], axis=0)
                next = dr.find_element_by_css_selector("input[alt='>']")
                next.click()
                sleep(6)
        except:
            print('Done')
            if len(temp_df)>0:
                new_cols = [(b, x) for x in temp_df.columns]
                temp_df.columns = pd.MultiIndex.from_tuples(new_cols)
            if len(final_df) > len(temp_df):
                final_df = pd.concat([final_df, temp_df], axis=1)
            else:
                final_df = pd.concat([temp_df, final_df], axis=1)
            break
    print(b)
    print(final_df)

final_df.to_csv('task3.csv')