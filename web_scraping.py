""" perform webscraping of item reviews of an e-commerce website"""
from bs4 import BeautifulSoup
import time
import requests
html_text = requests.get('https://www.amazon.in/s?k=earbuds+bluetooth+wireless&crid=3L2U8X675ISDS&sprefix=ear%2Caps%2C987&ref=nb_sb_ss_ts-doa-p_9_3').text
#print(html_text)
soup=BeautifulSoup(html_text,'lxml')
ear_buds = soup.find_all('span',class_ = 'a-size-medium a-color-base a-text-normal')
#print(ear_buds)
bud_img = soup.find_all('img',class_ = "s-image")
print(bud_img)