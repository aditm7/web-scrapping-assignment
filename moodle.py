from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/aditmalhotra/Documents/geckodriver"

#inputting the user id and password
id = input("enter user id")
pas = input("enter password")

driver = webdriver.Firefox()
driver.get("https://moodle.iitd.ac.in/login/index.php")

#ouputting the user data in respective feilds
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )    
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")  
    username.send_keys(id)
    password.send_keys(pas)  

    #solving the captcha
    l=main.text.split("\n")
    t=l[3]
    s=t.split(" ")
    if s[1]=="add":
        c = int(s[2]) + int(s[4])
    elif s[1]=="subtract":
    	c = int(s[2]) - int(s[4])
    elif s[2]=="first" or s[2]=="second":
    	c = int(s[4]) + int(s[6])

    #clicking the final submit button
    j = driver.find_element_by_id("valuepkg3")
    j.clear()
    j.send_keys(c)
    button = driver.find_element_by_id("loginbtn")
    button.click()

except:
    driver.quit()
