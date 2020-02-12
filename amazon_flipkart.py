from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone xr")
driver.find_element_by_xpath("//span[contains(text(),'Go')]/../input").click()
driver.find_element_by_xpath("//span[contains(text(),'Apple iPhone XR (64GB) - Yellow')]").click()
handles=driver.window_handles
driver.switch_to.window(handles[1])
amazon_price=driver.find_element_by_xpath("//span[@id='priceblock_dealprice']").text
amazon=amazon_price[2:-3]
s1=str(amazon)
i1=s1.replace(",","")
amazon_v1=int(i1)

#java script code to open new tab
driver.execute_script("window.open('https://www.flipkart.com/','tab1')")
driver.switch_to.window('tab1')
driver.find_element_by_xpath("//button[text()='✕']").click()
driver.find_element_by_name("q").send_keys("iphone xr")
driver.find_element_by_xpath("//button[@type='submit']").click()
import time
time.sleep(3)
driver.find_element_by_xpath("//div[contains(text(),'Apple iPhone XR (Yellow, 64 GB)')]").click()
handle=driver.window_handles
driver.switch_to.window(handle[3])
flipkart_price=driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
flipkart=flipkart_price[1:]
s2=str(flipkart)
i2=s2.replace(",","")
flip_v2=int(i2)
try:
    assert amazon_v1>=flip_v2,"Price is less in flipkart"
    print("price is less in Amazon ")
finally:
    driver.quit()
