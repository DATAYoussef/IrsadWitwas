# This is a sample Python script.

# press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium.webdriver.common.by import By
from selenium import webdriver
import time


website = 'https://www.tapology.com/rankings/groups/current'
path = 'Home/Downloads/chromedriver_linux64(1)'
driver = webdriver.Chrome(path)
driver.get(website)

top_heavyweight_button = driver.find_element(By.LINK_TEXT, "Top Heavyweights - 265 lbs.")
time.sleep(1)
top_heavyweight_button.click()
time.sleep(1)

top_heavyweight_names_wrecords = driver.find_elements(By.CLASS_NAME, 'rankingItemsItemRow')

top_heavyweight_names_wrecords_list = []
for name in top_heavyweight_names_wrecords:
    # print(name.text)
    top_heavyweight_names_wrecords_list.append(name.text)

# print('......')
# for i in range(7):
#     list(top_heavyweight_names_wrecords)[i].text
for person in top_heavyweight_names_wrecords_list:
    name_record = person.split(sep='\n')
    name = name_record[0]
    record = name_record[1]
    print(name)
    print(f'{name_record[0]} heeft een record van: {name_record[1]}')

driver.quit()