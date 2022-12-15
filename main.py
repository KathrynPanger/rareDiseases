from selenium import webdriver
from selenium.webdriver.common.by import By
PATH = "/home/ygael/Code/rareDiseases/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=PATH)

#Open Browser
mainPage = "https://rarediseases.org/for-patients-and-families/information-resources/rare-disease-information/"
driver.get(mainPage)

#Close Annoying Popup
xButtonClass = "popmake-close"
xButtons = driver.find_elements(By.CLASS_NAME, xButtonClass)
xButtons[0].click()

#Get links to search result pages


#Get all result links on each page


