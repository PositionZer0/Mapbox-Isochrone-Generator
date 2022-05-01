import csv
import requests
import geopandas
import matplotlib.pyplot as plt

import json

YOUR_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

f = open('data.csv', 'r')
csvreader = csv.reader(f)
final_list = list(csvreader)[1:]

first = final_list[0]
url = 'https://api.mapbox.com/isochrone/v1/mapbox/{}/{}%2C{}?contours_minutes={}&polygons=true&access_token={}'.format(first[1],first[2],first[3],first[-1],YOUR_ACCESS_TOKEN)
page = requests.get(url)
page = page.content
page = page.decode('utf-8')
page = json.loads(page)
page = json.dumps(page, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
page = eval(page)
features = page['features']
features[0]['properties']['ID']=first[0]
features[0]['properties']['profile']=first[1]
features[0]['properties']['longitude']=first[2]
features[0]['properties']['latitude']=first[3]
features[0]['properties']['contours_minutes']=first[-1]

for ele in final_list[1:]:
    url = 'https://api.mapbox.com/isochrone/v1/mapbox/{}/{}%2C{}?contours_minutes={}&polygons=true&access_token={}'.format(ele[1],ele[2],ele[3],ele[-1],YOUR_ACCESS_TOKEN)
    data = requests.get(url)
    data = data.content
    data = data.decode('utf-8')
    data = json.loads(data)
    data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    data = eval(data)
    geom = data['features']
    geom[0]['properties']['ID']=ele[0]
    geom[0]['properties']['profile']=ele[1]
    geom[0]['properties']['longitude']=ele[2]
    geom[0]['properties']['latitude']=ele[3]
    geom[0]['properties']['contours_minutes']=ele[-1]

    features.append(geom[0])

page=json.dumps(page)
page=json.loads(page)
page=json.dumps(page, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)

with open('geodata.json','w') as f:
    f.write(page)

data=geopandas.read_file('geodata.json')
print(data)
data.to_file('data', encoding='utf-8')
map = data.geometry.plot()
plt.savefig('data.jpg')