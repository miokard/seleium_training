from selenium import webdriver

driver = webdriver.Chrome('D:\projects\gmail\chromedriverGA\chromedriver.exe')
url = 'https://www.google.com/'

driver.get(url)

driver.close()
