from sys import api_version
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key =False
if api_key is False:
    api_key =42
    webservice = 'http://py4e-data.dr-chuck.net/json?'
else:
    webservice = 'http://maps.googleapis.com/maps/api/geocode/json?'
    
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    
    keeps = dict()
    keeps['address'] = address
    if api_key is not False:
        keeps['key'] = api_key
    url = webservice + urllib.parse.urlencode(keeps)
    
    print('Retrieving', url)
    resloc = urllib.request.urlopen(url, context=ctx)
    data = resloc.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    
    json.dumps(js, indent=4)
    place = js['results'][0]['place_id']
    print ('PLace Id', place)