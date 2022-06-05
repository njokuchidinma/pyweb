from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



#Ignore SSL certificates errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


numbers = soup.find_all("span", {"class":"comments"})
total = sum([int(number.text) for number in numbers])
print(total)

#nums = list()
#http://py4e-data.dr-chuck.net/comments_1512917.html
#for tag in soup.find_all(re.compile("^[0-9]+")):
    #print(tag.number)
#print(soup.find_all(""))
#num = numbers[0]
#for i in numbers:
    #nums.append(i.get_num())   
     
#print(numbers)