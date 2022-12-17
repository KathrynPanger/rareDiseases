import re
from bs4 import BeautifulSoup
class Disease():
    def __init__(self, fileName, webpage):
        self.fileName = fileName
        self.diseaseId = hash(fileName)
        self.webpage = webpage
        self.corpus = self.getPageText(self.fileName)
        self.wordBag = self.getWordBag(self.corpus)
    def getWordBag(self, textBody: str):
        regex = re.compile('[^a-zA-Z]')
        wordCounts = {}
        for item in textBody.split():
            item = regex.sub('', item)
            if item not in wordCounts:
                wordCounts[item] = 1
            else:
                wordCounts[item] += 1
        return wordCounts
    def getPageText(self, filename):
        file = open(filename).read()
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