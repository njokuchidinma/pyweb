import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sums = 0
tally = ()
resloc = input("Enter - ")
reslocate = resloc + urllib.parse.urlencode(tally)
url = urllib.request.urlopen(reslocate, context=ctx)

data = url.read()

stuff = ET.fromstring(data)

lst = stuff.findall('comments/comment')

for item in lst:
    num = int(item.find('count').text)
    sums += num
print (sums)
#for count in  stuff.findall('.//count'):
    #rank = count.find('count').text
   # print(rank) 
#counts = stuff.findall('.//count')

#print(counts)