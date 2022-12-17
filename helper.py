import re

def onlyInts(list):
    integerList = []
    for item in list:
        try:
            int(item)
            integerList.append(item)
        except:
            continue
    return integerList

def getDisease(driverElement, driver):
    diseaseName = driverElement.text
    driverElement.click()
    with open(f"webpages/{diseaseName}.html", "w") as f:
        f.write(driver.page_source)


def closePopup():
    try:
        xButtonClass = "popmake-close"
        xButtons = driver.find_elements(By.CLASS_NAME, xButtonClass)
        xButtons[0].click()
    except:
        pass

    def getCorpus(textBody: str):
        regex = re.compile('[^a-zA-Z]')
        alphabeticalOnly = regex.sub('', textBody)
        wordCounts = {}
        for item not in alphabeticalOnly.split():
            if item in wordcounts:
                wordcounts[item] = 1
            else:
                wordcounts[item] += 1
        return wordCounts