import requests
from bs4 import BeautifulSoup


#define the scrapping site
url='https://www.geeksforgeeks.org/fundamentals-of-algorithms/?ref=header_outind'

#send a get request for hosted server
response = requests.get(url)

#check the status of request
if response.status_code==200:
    soup = BeautifulSoup(response.text,'html.parser')
    
    h1_tags = soup.find_all('h1')
    print(h1_tags)

    className = 'text'

    para = soup.find_all('p')
    
for p 

    
else:
    print("Error..")