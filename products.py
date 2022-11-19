from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd

url ='https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
request = requests.get(url)
htmlcontent = request.content
soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup.prettify)

products=[]
prices=[]
ratings=[]
product=soup.find('div',attrs={'class':'_4rR01T'})
print(product.text)

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):

  name=a.find('div',attrs={'class':'_4rR01T'})
  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
  rating=a.find('div',attrs={'class':'_3LWZlK'})
  products.append(name.text)
  prices.append(price.text)
  ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products,'Prices':prices,'Ratings':ratings})
df.head()
df.to_csv('products.csv')