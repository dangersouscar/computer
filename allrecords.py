import requests
import json
import pandas as pd
res =eval(requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx9c048661b35d1f57&secret=5e618115adc71a3f8f926aba4b611479').text.replace(" ,",""))
print(isinstance(res,dict),res)
access_token=res["access_token"]
print(access_token)
url = 'https://api.weixin.qq.com/tcb/databasequery?access_token='+access_token
res =eval(requests.post('https://api.weixin.qq.com/tcb/databasemigrateexport?access_token='+access_token).text.replace(" ,",""))
body = { "env":"cdh1-61abq","query": "db.collection(\"allrecords\").limit(1000).skip(0).get()"}
response = requests.post(url, data = json.dumps(body))
##url = 'https://api.weixin.qq.com/tcb/databasemigratequeryinfo?access_token='+access_token
response = requests.post(url, data = json.dumps(body))
data=eval(response.text.replace("\/","/"))['data']
print(data)
list=[]
for i in data:
    value=eval(i)
    list.append(value)
pd.DataFrame(list).to_csv('维修记录.csv')
