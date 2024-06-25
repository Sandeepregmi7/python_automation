from bs4 import BeautifulSoup
import requests

url="https://www.icc-cricket.com/tournaments/t20cricketworldcup/index"
responce=requests.get(url)
soup=BeautifulSoup(responce.text,'html.parser')

imagetag=soup.find_all('img')
i=1
for imagetag in imagetag:
    image_link=imagetag['src']
    
    if image_link.startswith('http'):
        print(f"image source link: {image_link}")
        
        image_data=requests.get(image_link).content
        
        with open(f'image {i}.jpg','wb') as files:
            files.write(image_data)
        i+=1