import json

f = open('../data/data/20200117.json')

json1 = json.loads(f.read())
for i in json1['features']:
  # print(i['properties'])
  if i['properties']['省份']=='山东省':
    print(i['properties'])