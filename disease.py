class disease():
    def __init__(self, name, webpage):
        self.name = name
        self.diseaseId = hash(name)
        self.webpage = webpage
        self.corpus = []
        self.wordBag = {}
