from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import date, datetime, timedelta


base_date = '2021-09-19'
date_t = date.today()
number = date_t - base_date
url = "https://xkcd.com/"+str(number)
urlreq = requests.get(url)
html = BeautifulSoup(urlreq.content, "html.parser")

html_title = html.find("div", id="ctitle")

urls = [a["href"] for a in html.find_all('a', href=True) if a["href"][a["href"].rfind(".")+1:] in ["jpeg", "png", "jpg"]]
url_value= urls[0]
title = html_title.get_text()
print(title)
print(url_value)

filename = '/home/ubuntu/files/xkcdfolder/'+'('+str(number)+')'+'-'+str(title)+".jpg"

urllib.request.urlretrieve(url_value, filename)