import requests
import json
import sqlite3
import time
import datetime
import numpy as np
con=sqlite3.connect("db")
cur = con.cursor()
print(con)
import pandas as pd
res =eval(requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx9c048661b35d1f57&secret=5e618115adc71a3f8f926aba4b611479').text.replace(" ,",""))
print(isinstance(res,dict),res)
access_token=res["access_token"]
print(access_token)
url = 'https://api.weixin.qq.com/tcb/databasequery?access_token='+access_token
body = { "env":"cdh1-61abq","query": "db.collection(\"addresslist\").limit(1000).skip(0).get()"}
response = requests.post(url, data = json.dumps(body))
##print(response.text)
data=eval(response.text)['data']
list=[]
for i in data:
    value=eval(i)
    
    list.append(value)
result=pd.DataFrame(list)
##result.to_csv('addresslist.csv')
##print(result.iloc[:,[2,3,4]])
name=result.iloc[:,3].values.tolist()

value=result.iloc[:,2]
member = value.values.tolist()
print(member)
now_time = datetime.datetime.now().strftime('%F %T')
print(now_time)
member.append(now_time)
print(name.append("数据更新时间"))
list1=[]
list1.insert(0,member)
print(member)
print(dir(member))
df = pd.DataFrame(list1, columns=name)
print(df)
df.to_sql(name=str("addresslist1"), con=con, if_exists='append', index=None)


