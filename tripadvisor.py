from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tripadvisor.in/")
driver.find_element_by_name("q").send_keys("Club Mahindra")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("//span[text()='Club Mahindra Varca Beach']").click()
handle1=driver.window_handles
driver.switch_to.window(handle1[1])
driver.find_element_by_xpath("//a[contains(text(),'Write a review')]").click()
handle2=driver.window_handles
driver.switch_to.window(handle2[2])
mouse=driver.find_element_by_xpath("//em[contains(text(),'Excellent') and @id='overallRatingFlagText']")
act=ActionChains(driver)
act.move_to_element(mouse).perform()
mouse.click()
driver.find_element_by_name("ReviewTitle").send_keys("Good Experience")
driver.find_element_by_id("ReviewText").send_keys("Before I started my own adventure travel blog 9 years ago, I was inspired to explore the world after reading other people’s travel blogs online. Travel blogs are a wonderful source for cool ideas & advice if you’re planning a trip! Below you’ll find some of my favorite travel blogs, plus many more I’ve discovered over the years.")
ratings=driver.find_elements_by_xpath("//div[@class='ratingBubbleTable']")
for rate in ratings:
    rate.click()
driver.find_element_by_name("noFraud").click()
driver.find_element_by_id("SUBMIT").click()