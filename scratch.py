import os
from bs4 import BeautifulSoup
os.chdir("webpages")
directory = os.listdir()
file = open(directory[0]).read()
soup = BeautifulSoup(file, features="html.parser")
content = soup.find_all("div", {"class": "rdr-box"})
for item in content:
    print(item.text)