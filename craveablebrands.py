from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get('https://craveablebrands.macromatix.net/MMS_Logon.aspx')

username = 'Kesh.Tummala'
password = 'Kesh.Tummala'

driver.find_element_by_id('Login_UserName').send_keys(username)
driver.find_element_by_id('Login_Password').send_keys(password)


driver.find_element_by_id('Login_Button1').click()


table = driver.find_element_by_id('ctl00_ph_DatagridSalesResults')

trs = table.find_elements_by_tag_name('tr')

values = []
for tr in trs:
    try:
        td = tr.find_elements_by_tag_name('td')[1].find_element_by_tag_name('input')
        values.append(td.get_attribute('value'))
    except:
        pass

labels = ['ST CLAIR', 'ROUSE HILL', 'CARLTON', 'Total']

for value, label in zip(values, labels):
    print(label,"=",value)

driver.quit()