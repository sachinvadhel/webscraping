from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd
import logging

# supress log messages
logging.getLogger("requests").setLevel(logging.WARNING)

def get_content(url):
  request = requests.get(url)
  htmlcontent = request.content
  soup = BeautifulSoup(htmlcontent,"html.parser")

  products=[]
  prices=[]
  ratings=[]
  product=soup.find('div',attrs={'class':'_4rR01T'})

  for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):

    name=a.find('div',attrs={'class':'_4rR01T'})
    price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div',attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

  df = pd.DataFrame({'Product Name': products,'Prices':prices,'Ratings':ratings})
  return df

# parse all pages for category apple
# first page
dfs = products.get_content("https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=apple&otracker=categorytree")
# pages 2 to 11
for i in range(2, 12):
  df=products.get_content("https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=apple&otracker=categorytree&page="+str(i))
  dfs=pd.concat([dfs, df])

# print cheapest phone per product name
print(dfs.groupby("Product Name").min())
