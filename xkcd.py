from bs4 import BeautifulSoup
import requests
number = 1
url = "https://xkcd.com/"+str(number)
urlreq = requests.get(url)
html = BeautifulSoup(urlreq.content, "html.parser")
print(html)

html_title = html.find("div", id="ctitle")
title = html_title.get_text()
print(title)


