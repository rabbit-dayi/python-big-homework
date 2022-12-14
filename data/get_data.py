#Get Data URL:https://2019ncov.chinacdc.cn/JKZX/yq_20221213.json

import requests
import datetime
# from bs4 import BeautifulSoup #pip install bs4
from fake_useragent import UserAgent  #pip install fake-useragent

import json


d1 = datetime.timedelta(days=1) #天数变化值
date = datetime.datetime(year=2019,month=12,day=20)#日期变量

for i in range(999999):
  str_day=date.strftime("%Y%m%d")
  url_str='https://2019ncov.chinacdc.cn/JKZX/yq_{}.json'.format(str_day)#生成url
  ua = UserAgent()
  headers={'User-Agent':ua.random}
  
  res = requests.get(url_str,headers=headers)
  if res.status_code==200:
    f=open("./data/"+str_day+".json","w")
    j = json.loads(res.content) #读取json
    f.write(json.dumps(j)) #写入json格式
    f.close()
  else:
    attempt=0
    while attempt<=3 and res.status_code!=200:
      try:
        res = requests.get(url_str,headers=headers)
        if(res.status_code!=200):
          print([401,"[dayi-error]"+str_day+" error:{}".format(attempt)])
        attempt+=1
      except:
        print([501,"[dayi-error]"+str_day+" error:{}".format(attempt)])
        attempt+=1
        pass
  
  date+=d1#天数加一天
  print(url_str)
  if date>=datetime.datetime.today():
    break


# for i in range()