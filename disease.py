import re
from bs4 import BeautifulSoup
class Disease():
    def __init__(self, name, webpage):
        self.name = name
        self.diseaseId = hash(name)
        self.webpage = webpage
        self.corpus = []
        self.wordBag = {}
    def getWordBag(self, textBody: str):
        regex = re.compile('[^a-zA-Z]')
        alphabeticalOnly = regex.sub('', textBody)
        wordCounts = {}
        for item in alphabeticalOnly.split():
            if item not in wordCounts:
                wordCounts[item] = 1
            else:
                wordCounts[item] += 1
        return wordCounts
    def getPageText(self, webpage):
        file = open(webpage).read()
        soup = BeautifulSoup(file, features="html.parser")
        omitableDivList = ["acknowledgment", "references", "years_published",
                           "disclaimer", "supporting-organizations",
                           "resources"]
        for unwantedDiv in omitableDivList:
            for div in soup.find_all("div", {'id': f'{unwantedDiv}'}):
                div.decompose()
        medicalText = soup.find_all("div", {"class": "rdr-box"})
        corpus = ""
        for item in medicalText:
            text = item.text
            corpus = corpus + " " + text
        return corpus