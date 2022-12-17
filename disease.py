import re
class disease():
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
        for item not in alphabeticalOnly.split():
            if item in wordcounts:
                wordcounts[item] = 1
            else:
                wordcounts[item] += 1
        return wordCounts