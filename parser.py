from request_data import request 
import json



keys = set()

# it return all keys for all avalible page
def get_all_cars(i):
    api = 'https://v3-111-2.gsl.feature-app.io/bff/car/search'
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
    params['page'] = i
    
    responce = request(api,params)
    if not responce:
        return
    all_data = json.loads(responce)
    cars = all_data.get('cars')
    if not cars:
        return
    for car in cars:
        keys.add(car.get('key'))

    print(i)
    return list(keys)

# it featch data for given key
def car_data(key):
    # it is api key for single car data 
    api ='https://v3-111-2.gsl.feature-app.io/bff/car/get'
    # params was use for add dynamic keys 
    params = {
        'key': key,
        'country': 'GB',
        'endpoint': '{"endpoint":{"type":"publish","country":"gb","language":"en","content":"onehub_pkw","envName":"prod","testScenarioId":null},"signature":"ZWQcGYMemGx1hkFO4sq/vKJYYBJSVGPXQR7rMDs6BpE="}',
        'language': 'en',
        'market': 'passenger',
        'oneapiKey': 'nOqkwPxxu8ViK9aaHvTkglzVZAlX4yIx',
        'dataVersion': '640B4505742CCF6F343556C288EFEC22',
    }

    responce = request(api,params)
    # it check responce
    if not responce:
        return
    all_data = json.loads(responce)

    car_type = all_data.get('carTypeLabel'),
    car_key = all_data.get('key'),
    car_name = all_data.get('title'),
    sub_title = all_data.get('subtitle').get('value'),
    deler = {
                'name':all_data.get('dealer').get('name').get('value'),
                'phone':((all_data.get('dealer') or {}).get('phone') or {}).get('value'),
                'address':all_data.get('dealer').get('street').get('value') + all_data.get('dealer').get('zip').get('value') +all_data.get('dealer').get('city').get('value')
            }
    fule= all_data.get('motor').get('fuel').get('value')
    capacity = ((all_data.get('motor') or {}).get('capacity') or {}).get('value')
    power_kw= all_data.get('motor').get('powerKw').get('value') + all_data.get('motor').get('powerKw').get('unit')
    color= ((all_data.get('color',{}).get('out',{})).get('value'))
    images = [i.get('href') for i in all_data.get('images')]
    price = all_data.get('parsedPrice').get('value')
    price_unit = all_data.get('parsedPrice').get('unit')

    vehicle_data = {
        'engine':fule + "|" +power_kw ,
        'model_year' : all_data.get('modelyear').get('value'),
        'drive_type': all_data.get('drive').get('value'),
        'gear_type':all_data.get('gear').get('value'),
        'noise_level' : all_data.get('noiseLevel')
    }

    equipment_tabs = [{
        e.get('headline'): { i.get('headline') : ",".join(v.get('text') for v in i.get('values')) for i in e.get('items')} 
    }for e in all_data.get('equipmentTabs') if e.get('items')]

    finance_data = all_data.get('hypermediaFinancing')

    finanace = {
        k: v for k, v in (finance_data.get('default') or {}).items()
    } if finance_data else {}


    # final dict for single car
    data = {
        'car_type':"".join(car_type) or None,
        'car_name':"".join(car_name)or None,
        'sub_title':"".join(sub_title) or None,
        'capacity':capacity,
        'delers':deler or None,
        'fule':fule or None,
        'color':color or None,
        'images':images or None,
        'price':price or None,
        'price_unit':price_unit or None,
        'vehicle_data':vehicle_data or None,
        'equipment':equipment_tabs or None,
        'finance':finanace or None
    }

    # with open('s2.json','w',encoding='utf-8') as f:
    #     json.dump(data,f,indent=4,default=str)

    print(f"{key} was added!!")
    return data


