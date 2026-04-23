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

# it is use to get all pages count
pagedata = json.loads(request('https://v3-111-2.gsl.feature-app.io/bff/car/search',params))
lastindex = pagedata.get("meta").get("pageMax")

# this thread was work for get keys
with ThreadPoolExecutor(max_workers=5) as e:
    e.map(get_all_cars,range(1,lastindex+1))

# this thread was works for featch data 
with ThreadPoolExecutor(max_workers=5) as e:
    #car data was data parser it extract data for key
    result = list(e.map(car_data,keys))
    row = []
    for r in result:
        #data append in row and volks_vagon list for storeing
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

if row:
    insert_data(row)



