import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tally = 0
loc = input("Enter: ")
location = urllib.request.urlopen(loc)
data = location.read()
info = json.loads(data)
print('Retrieving', loc)
print('Retrieved', len(data), 'characters')

count_values = [ el['count'] for el in info['comments'] ] 
print (sum(count_values))
    