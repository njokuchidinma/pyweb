import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mde = ssl.CERT_NONE

nums = 0
iterate = 0
url = input("Enter - ")
spot = int(input("Enter position: "))
number = int(input("Enter count:"))

while nums < number:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')

   tags = soup('a')
   for tag in tags:
     iterate = iterate + 1
     if iterate == spot:
        url = tag.get('href', None)
        print ("Retrieving:", url)
        iterate = 0
        break
   nums = nums + 1