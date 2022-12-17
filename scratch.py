import os
from bs4 import BeautifulSoup
os.chdir("webpages")
directory = os.listdir()
file = open(directory[0]).read()
soup = BeautifulSoup(file, features="html.parser")
omitableDivList = ["acknowledgment", "references", "years_published", "disclaimer", "supporting-organizations", "resources"]
for unwantedDiv in omitableDivList:
    for div in soup.find_all("div", {'id': f'{unwantedDiv}'}):
        div.decompose()
medicalText = soup.find_all("div", {"class": "rdr-box"})
for item in medicalText:
    item = item.text
    print(item)


#don't forget extract()