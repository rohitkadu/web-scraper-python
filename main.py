# Web Scraper 
# Libraries Used :
# 1. requests ( pip install requests )
# 2. bs4 ( pip install bs4 )
# 3. html5lib ( pip install html5lib

import requests
from bs4 import BeautifulSoup

# url = "your url here"
url = "https://www.moneycontrol.com/stocksmarketsindia/"

# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the HTML 
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


# Step 3 : HTML tree traversal 

# The four major and important objects are : 
# 1. BeautifulSoup --> print(type(soup))
# 2. Tag --> print(type(title))
# 3. NavigableString --> print(type(title.string))
# 4. Comments

# Get the Title of the Page 
title = soup.title
# print((title.string))

# Get all meta tags 
metaTags = soup.find_all('meta')
# print(metaTags)

# Get all p tags 
pTags = soup.findAll('p')
# print(pTags)

# Get first element in HTML tag 
# print(soup.find('p'))

# Get class of any element in HTML page 
# print(soup.find('p')['class'])

# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all a tags 
anchorTags = soup.find_all('a')
# print(anchorTags)
# for links in anchorTags:
#     print(links.get('href'))

# Get all images on the HTML page 
imgs = soup.find_all('img')
# print(imgs)
# for srcs in imgs:
#     print(srcs.get('src'))


# for more / advanced scraping 
# go to : https://www.crummy.com/software/BeautifulSoup/bs4/doc/