from selenium import webdriver


driver = webdriver.Chrome('/home/alejandro/Desarrollo de Software/Laboratorio4/chromedriver')
driver.get("https://www.python.org")
boton = driver.find_element_by_xpath('//*[@id="news"]/a')
boton.click()
input = driver.find_element_by_xpath('//*[@id="id-search-field"]')
input.send_keys('disc')
boton.clear()
