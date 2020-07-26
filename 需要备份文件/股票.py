import tushare as ts
import pandas as pd
import numpy as np
import sqlite3
import time
import datetime
con=sqlite3.connect("db")
cur = con.cursor()
print(con)
ts.set_token("030340d5dee462cf170d55e914589d0f530f8bac1f067bd94c87b2a4")
pro = ts.pro_api()
##############################################################################

def stockholder ():
    data = ts.fund_holdings(2019, 4)
    data.to_sql('stockholder', con=con, if_exists='append', index=None)




##############################################################################
def upinformation (ts_code):
    ts_code=ts_code
    end_date = time.strftime("%Y%m%d",time.localtime(time.time()))
    def get_date(days):
        start_date=datetime.datetime.now() - datetime.timedelta(days = days)
        return str(start_date)[0:10].replace("-", "" )
    print(str(ts_code))
    start_date1=get_date(5000)
    start_date2=get_date(10000)
    start_date3=get_date(15000)
    df1 = pro.daily(ts_code=ts_code, start_date=start_date1, end_date=end_date)
    df2 = pro.daily(ts_code=ts_code, start_date=start_date2, end_date=start_date1)
    df3 = pro.daily(ts_code=ts_code, start_date=start_date3, end_date=start_date2)

    dataset1=pd.DataFrame(df1)
    dataset2=pd.DataFrame(df2)
    dataset3=pd.DataFrame(df3)
    dataset1.to_sql(name=str(ts_code), con=con, if_exists='replace', index=None)
    dataset2.to_sql(name=str(ts_code), con=con, if_exists='append', index=None)
    dataset3.to_sql(name=str(ts_code), con=con, if_exists='append', index=None)
    
##############################################################################
def stockname ():
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_sql('stock_basic', con=con, if_exists='append', index=None)
##############################################################################
def allstock():
    cur.execute("select ts_code from  stock_basic")
    rows = cur.fetchall()
    rows = np.array(rows)  
    for i in range(len(rows)):
        time.sleep(0.5)
        try:
            upinformation (str(rows[i][0]))
        except OSError:
            pass
        continue
##############################################################################
def get_h_data ():
    data = ('002352.SZ') #前复权
    data.to_sql('深圳', con=con, if_exists='append', index=None)
##############################################################################
def fund_basic ():
    data = pro.fund_basic(market='E')
    print(data)
    data.to_sql('fund_basic', con=con, if_exists='append', index=None)
##############################################################################
##stockname()
##allstock()
##stockholder()
##fund_basic ()
##ts_code="600690.SH"
fund_basic()





