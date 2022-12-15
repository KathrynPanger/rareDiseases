from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from helper import closePopup
from helper import onlyInts, getDisease
PATH = "/home/ygael/Code/rareDiseases/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=PATH)

#Open Browser
mainPage = "https://rarediseases.org/for-patients-and-families/information-resources/rare-disease-information/"

#Close Annoying Popup
def closePopup():
    try:
        xButtonClass = "popmake-close"
        xButtons = driver.find_elements(By.CLASS_NAME, xButtonClass)
        xButtons[0].click()
    except:
        pass


#Get links to search result pages

urlExtension = "page/x/"
#pageClass = "pagination"
# pages = driver.find_elements(By.CLASS_NAME, pageClass)
# lastPageNumber = int(max(onlyInts([item.text for item in pages])))
lastPageNumber = 65
paginationList = []
for i in range(lastPageNumber - 1):
    pageExtension = urlExtension.replace("x", str(i+1))
    pageUrl = mainPage + pageExtension
    paginationList.append(pageUrl)

#Get all result links on current page
diseaseClass = "rdr-one-title"


for page in paginationList[9:]:
    driver.get(page)
    closePopup()
    thisPageDiseases = driver.find_elements(By.CLASS_NAME, diseaseClass)
    diseases= {}
    for item in thisPageDiseases:
        diseases[item.text.replace("/","")] = item.get_attribute("innerHTML").split("\"")[1]
    for name, url in diseases.items():
        driver.get(url)
        with open(f"webpages/{name}.html", "w") as f:
            f.write(driver.page_source)