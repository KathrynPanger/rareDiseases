from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import onlyInts
PATH = "/home/ygael/Code/rareDiseases/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=PATH)

#Open Browser
mainPage = "https://rarediseases.org/for-patients-and-families/information-resources/rare-disease-information/"
driver.get(mainPage)

#Close Annoying Popup, If It Comes Up
try:
    xButtonClass = "popmake-close"
    xButtons = driver.find_elements(By.CLASS_NAME, xButtonClass)
    xButtons[0].click()
except:
    pass

#Get links to search result pages

urlExtension = "/page/x/"
pageClass = "pagination"
pages = driver.find_elements(By.CLASS_NAME, pageClass)
lastPage = max(onlyInts([item.text for item in pages]))

#Get all result links on current page
diseaseClass = "rdr-one-title"
thisPageDiseases = driver.find_elements(By.CLASS_NAME, diseaseClass)
diseaseList = [item.text for item in thisPageDiseases]