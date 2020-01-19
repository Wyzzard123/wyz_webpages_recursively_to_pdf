"""Proof of concept. Using https://www.edureka.co/blog/web-scraping-with-python/ """

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas 
import os

CHROMIUM_DRIVER = str(os.environ.get("CHROMIUMDRIVERPATH"))
driver = webdriver.Chrome(f"{CHROMIUM_DRIVER}")

products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
    name = a.find('div', attrs={'class':'_3wU53n'})
    price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating = a.find('div',  attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pandas.DataFrame({'Product Name':products, 'Prices':prices,'Rating':ratings})

df.to_csv('products.csv', index=False, encoding='utf-8')