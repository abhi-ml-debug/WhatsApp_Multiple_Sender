from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome('./chromedriver.exe')
char='y'
contacts=[]
while char=='y':
 x=input("Enter contact (case sensitive):\n")
 contacts.append(x)
 char=input("Want to enter more contacts? (y/n) \n")
msg=input("Enter the message\n")
freq=int(input("Enter the frequency\n"))

driver.get("https://web.whatsapp.com")
search_bar_path = "//*[@id=\"side\"]/div[1]/div/label/div/div[2]"
msg_bar_path="//*[@id=\"main\"]/footer/div[1]/div[2]/div/div[2]"
#The message bar's and search bar's XPath can be obtained 
#by doing a right click, inspecting element, and selecting "Copy XPath" of the required element  

for contact in contacts:
 driver.implicitly_wait(40)
 #Wait till a maximum of 40 seconds (Needed for QR code scan for first time)
 #Stop waiting as soon as search bar is found 
 element=driver.find_element_by_xpath(search_bar_path)
 element.click()
 time.sleep(2)
 element.send_keys(contact)
 time.sleep(2)
 element.send_keys(Keys.ENTER)
 element=driver.find_element_by_xpath(msg_bar_path)
 element.click()
 time.sleep(2)
 
 for i in range(freq):
  element.send_keys(msg)
  element.send_keys(Keys.ENTER)
  time.sleep(1)

driver.quit()
