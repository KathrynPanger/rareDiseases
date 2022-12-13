from selenium import webdriver
PATH = "/home/ygael/Code/rareDiseases/chromedriver"
driver = webdriver.Chrome(PATH)
url = "https://rarediseases.org/for-patients-and-families/information-resources/rare-disease-information/"
driver.get(url)
rdr-one-title
