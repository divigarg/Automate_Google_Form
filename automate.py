#!/usr/bin/env python
# coding: utf-8

# In[50]:


import time
from selenium import webdriver
NAME=input("Enter the Name:").strip()
ROLL_NO=input("Enter the Roll no:").strip()
KEY=input("Are you using python? Yes/No/Maybe:").strip()
URL=input("Enter the link to Github repo:").strip()
RADIO={'Yes':1,'No':2,'Maybe':3}

driver=webdriver.Chrome("C:\\Users\divyansh\Desktop\chromedriver.exe")

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform')

for i in range(100):
    print("Running {}".format(i+1))
    while True:
        if driver.current_url=="https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/formResponse":
            break
        else:
            name=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
            roll_no= driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
            python_yes_no=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[{}]/label/div/div[2]/div/span'.format(RADIO[KEY]))
            github_url=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
            check=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/input')
            name.clear()
            roll_no.clear()
            github_url.clear()
            name.send_keys(NAME)
            roll_no.send_keys(ROLL_NO)
            python_yes_no.click()
            github_url.send_keys(URL)
            if (name.get_attribute('data-initial-value')==NAME and github_url.get_attribute('data-initial-value')==URL
                and roll_no.get_attribute('data-initial-value')==ROLL_NO and check.get_attribute('value')==KEY):
                time.sleep(1)
                submit=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
                submit.click()
                print("Done {}".format(i+1))
            time.sleep(2)
    new_form=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_form.click()
print("Hurray! Hundred times form submission is done.")
driver.quit()
