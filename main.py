from parser import * 
from concurrent.futures import ThreadPoolExecutor
import json
from db import *

create_db()


#  main page appi it return single page data 12 cars
page_api = 'https://v3-111-2.gsl.feature-app.io/bff/car/search'


# it return all keys for cars 
params = {
        't_manuf': 'BQ',
        't_reserved': 'false',
        'sort': 'DATE_OFFER',
        'sortdirection': 'ASC',
        'pageitems': '12',
        'page': '1',
        'country': 'GB',
        'endpoint': '{"endpoint":{"type":"publish","country":"gb","language":"en","content":"onehub_pkw","envName":"prod","testScenarioId":null},"signature":"ZWQcGYMemGx1hkFO4sq/vKJYYBJSVGPXQR7rMDs6BpE="}',
        'language': 'en',
        'market': 'passenger',
        'oneapiKey': 'nOqkwPxxu8ViK9aaHvTkglzVZAlX4yIx',
        'dataVersion': '640B4505742CCF6F343556C288EFEC22',
    }
pagedata = json.loads(request('https://v3-111-2.gsl.feature-app.io/bff/car/search',params))
lastindex = pagedata.get("meta").get("pageMax")


with ThreadPoolExecutor(max_workers=10) as e:
    e.map(get_all_cars,range(lastindex))


volks_vagon = []
with ThreadPoolExecutor(max_workers=5) as e:
    #car data was data parser it extract data for key
    result = e.map(car_data,keys)
    row = []
    for r in result:
        #data append in row and volks_vagon list for storeing
        volks_vagon.append(r)
        row.append((
            r.get('car_type'),
            r.get('car_name'),
            r.get('sub_title'),
            r.get('capacity'),
            json.dumps(r.get('delers')),
            r.get('fule'),
            r.get('color'),
            json.dumps(r.get('images')),
            r.get('price'),
            r.get('price_unit'),
            json.dumps(r.get('vehicle_data')),
            json.dumps(r.get('equipment')),
            json.dumps(r.get('finance')),
        ))
        
        # 100 data was add at the time
        if len(row) == 100:
            insert_data(row)


# it return final output json
with open('final.json','w',encoding='utf-8') as f:
    json.dump(volks_vagon,f,indent=4,default=str)

