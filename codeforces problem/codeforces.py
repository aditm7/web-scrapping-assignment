from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

#input of variables and creating a folder of the same name as contest no
c = int(input("enter contest no"))
parent_dir = "/Users/aditmalhotra/Documents/"
directory = str(c)
mainfolder = os.path.join(parent_dir, directory)
os.mkdir(mainfolder)

#creating the driver and opening the desired contest website
PATH = "/Users/aditmalhotra/Documents/geckodriver"
driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.get("https://codeforces.com/contest/" + str(c))

#a method to find how many problems and thus total no of aplhabets
element1 = driver.find_elements_by_xpath("//td[@class='id dark left']")
element2 = driver.find_elements_by_xpath("//td[@class='id left']")
try:
	element3 = driver.find_element_by_xpath("//td[@class='id bottom left']")
except:
	element3 = driver.find_element_by_xpath("//td[@class='id bottom dark left']")
finally:
	element = []
	a = len(element1) + len(element2)

	for i in range(0,a):
		if i%2==0:
			element.append(element1[int(i/2)])
		else:
			element.append(element2[int((i//2))])
	a = a+1
	element.append(element3)

	#creating a list of the problem's aplbhabets codes
	problem = []
	for i in element:
		problem.append(i.text)

	#now iterating every problem one by one and storing the neccessary data
	for j in problem:
		parent_dir1 = parent_dir + str(c) + "/"
		subfolder = os.path.join(parent_dir1, j)
		os.mkdir(subfolder)  #creating the respective subfolders of problems
		driver.implicitly_wait(2)
		driver.get("https://codeforces.com/contest/" + str(c) + "/problem/" + j)
		sleep(1)
		#creating the screenshot of the problem part only and not the whole page
		main = driver.find_element_by_class_name("problem-statement")
		main.screenshot("/Users/aditmalhotra/Documents/" + str(c) + "/" + j + "/" + j + ".png")
		#storing the input and output of sample test runs in the text files
		IO_list = driver.find_elements_by_tag_name("pre")
		for b in range(len(IO_list)):
			if b%2==0:
				fr = open("/Users/aditmalhotra/Documents/" + str(c) + "/" + j + "/input" + str(((b)//2)+1) + ".text", "w+" )
				fr.write(IO_list[b].text)
				fr.close()
			else:
				fr = open("/Users/aditmalhotra/Documents/" + str(c) + "/" + j + "/output" + str(((b)//2)+1) + ".text", "w+" )
				fr.write(IO_list[b].text)
				fr.close()

driver.quit()
















