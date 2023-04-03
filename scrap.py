import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/oppo~brand/pr?sid=tyy%2C4io&page=2")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_='_4rR01T')
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
#print(name)
ratings=soup.find_all('div',class_='_3LWZlK')
rating=[]
for i in ratings[0:10]:
    d=i.get_text()
    rating.append(d)
#print(rating)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
#print(price)

links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:10]:
    d='https://www.flipkart.com'+i['href']
    link.append(d)
#print(link)
df=pandas.DataFrame()
df['names']=name
df['ratings']=rating
df['prices']=price
df['links']=link

df.to_csv('Mobiles.csv')
print(df)