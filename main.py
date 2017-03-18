import requests
from bs4 import BeautifulSoup
import json
import os
print('Fetching links.....')
soup = BeautifulSoup(requests.get('https://liyin.date/links').text,'html5lib')
links=soup.select('li.md-links-item')
list={}
print('Checking links.....')
for link in links:
    url=link.find_all('a')[0].get('href') 
    try:
        response_link=requests.get(url,timeout=30)
        code=response_link.status_code
        timeelapsed=response_link.elapsed.total_seconds()
        print(url +' is ' + str(code) + ' in ' + str(timeelapsed) + 's')
        list[url]=str(code)
    except requests.exceptions.Timeout:
        print(url + ' is Timeout')
        list[url]='timeout'
    except requests.exceptions.SSLError:
        print(url + ' is SSLError')
        list[url]='sslerror'
statejson='state('+json.dumps(list)+')'
os.mkdir('public')
with open('public/data.jsonp', 'w') as outfile:
    outfile.write(statejson)