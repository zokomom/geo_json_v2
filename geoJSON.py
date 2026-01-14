import requests
import urllib.parse
import json

serviceurl = "https://api.geoapify.com/v1/geocode/search?"

while True:
    
    address=input("Enter Address : ")
    if not address:
        break
    key=input("Enter API key : ")
    if not key:
        print("please provide API key!!")
        continue
    
    params = {
        "text": address,
        "apiKey": key
    }
    
    url =  serviceurl + urllib.parse.urlencode(params)
    key_pos = url.find('&apiKey')
    if key_pos != -1:
        print("Retrieving......", url[:key_pos])
    else:
        print("Retrieving......")
    resp = requests.get(serviceurl, params=params)
    print("Status code is : ",resp.status_code)

    json_data=resp.json()

    if resp.status_code!=200:
        print("Data Not Retrieved")
    else:
        print("Retrieved",len(resp.text),"characters")

    print(json.dumps(json_data,indent=4,ensure_ascii=False))    

    useful_info={}


    if json_data and 'features' in json_data and len(json_data['features'])>0:
        useful_info['country']=json_data['features'][0]['properties'].get('country',None)
        useful_info['country_code']=json_data['features'][0]['properties'].get('country_code')
        useful_info['state']=json_data['features'][0]['properties'].get('state',None)
        useful_info['county']=json_data['features'][0]['properties'].get('county',None)
        useful_info['state_district']=json_data['features'][0]['properties'].get('state_district',None)
        useful_info['city']=json_data['features'][0]['properties'].get('city',None)
        useful_info['postcode']=json_data['features'][0]['properties'].get('postcode',None)
        useful_info['longitude']=json_data['features'][0]['properties'].get('lon',None)
        useful_info['latitude']=json_data['features'][0]['properties'].get('lat',None)
        useful_info['state_code']=json_data['features'][0]['properties'].get('state_code',None)
        useful_info['result_type']=json_data['features'][0]['properties'].get('result_type',None)
        useful_info['formatted']=json_data['features'][0]['properties'].get('formatted',None)
        useful_info['place_id']=json_data['features'][0]['properties'].get('place_id',None)
        for i,j in useful_info.items():
            print(i,'=',j)
    else:
        print("Address not exist !! Re-Check ur address...")
        