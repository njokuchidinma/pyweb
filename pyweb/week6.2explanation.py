import urllib.request,urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



#Stroring the given parameters
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
# sample_address = "South Federal University"
data_address = "IIT KANPUR"
address_wanted = data_address

#Setting the GET parameters on the URL
parameters = {"address": address_wanted, "key":api_key}
paramsurl = urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl.strip() + paramsurl.strip()
print("DATA URL: ", queryurl)

#Obtaining and reading the data
try :
    data_read = urllib.request.urlopen(queryurl , context=ctx).read()
    data = data_read.decode()
    # Parsing the data and looking for the field we want.
    jsondata = json.loads(data)
    print(jsondata)
    place_id = jsondata["results"][0]["place_id"]
    print("PLACE ID: ", place_id)
except:
    print("Error.....")
    print("-"*50)
    print(data)

#DATA URL:  http://py4e-data.dr-chuck.net/json?address=IIT+KANPUR&key=42
#{'results': [{'access_points': [], 'address_components': [{'long_name': 'Kalyanpur', 'short_name': 'Kalyanpur', 'types': ['political', 'sublocality', 'sublocality_level_1']}, {'long_name': 'Kanpur', 'short_name': 'Kanpur', 'types': ['locality', 'political']}, {'long_name': 'Kanpur Nagar', 'short_name': 'Kanpur Nagar', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Uttar Pradesh', 'short_name': 'UP', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'India', 'short_name': 'IN', 'types': ['country', 'political']}, {'long_name': '208016', 'short_name': '208016', 'types': ['postal_code']}], 'formatted_address': 'Kalyanpur, Kanpur, Uttar Pradesh 208016, India', 'geometry': {'location': {'lat': 26.5123388, 'lng': 80.2329}, 'location_type': 'GEOMETRIC_CENTER', 'viewport': {'northeast': {'lat': 26.5136877802915, 'lng': 80.23424898029151}, 'southwest': {'lat': 26.5109898197085, 'lng': 80.23155101970849}}}, 'place_id': 'ChIJcb6oxAE3nDkRNoTDq4Do-zo', 'plus_code': {'compound_code': 'G66M+W5 Kalyanpur, jvs tower, Kanpur, Uttar Pradesh, India', 'global_code': '7MR2G66M+W5'}, 'types': ['establishment', 'point_of_interest', 'university']}], 'status': 'OK'}
#PLACE ID:  ChIJcb6oxAE3nDkRNoTDq4Do-zo
