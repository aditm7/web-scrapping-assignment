from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

#input of variables and creating a folder of the name of desired difficulty problems
min = int(input("enter lower range of difficulty"))
max = int(input("enter upper range of difficulty"))
n = int(input("enter how many problems you need"))
parent_dir = "/Users/aditmalhotra/Documents/"
directory = "problems of difficulty range" + "(" + str(min) + "-" + str(max) + ")" 
mainfolder = os.path.join(parent_dir, directory)
os.mkdir(mainfolder)

k = int(n//100) + 1

#creating the driver and opening the desired difficulty problems 
PATH = "/Users/aditmalhotra/Documents/geckodriver"
driver = webdriver.Firefox()
driver.implicitly_wait(2)

for x in range (1,k+1):
	driver.get("https://codeforces.com/problemset/page/" + str(x) + "?tags=" + str(min) + "-" +str(max))
	element1 = driver.find_elements_by_xpath("//td[@class='id dark left']")
	element2 = driver.find_elements_by_xpath("//td[@class='id left']")
	element3 = driver.find_element_by_xpath("//td[@class='id bottom left']")
	element = []
	a = len(element1) + len(element2)

	for i in range(0,a):
		if i%2==0:
			element.append(element1[int(i/2)])
		else:
			element.append(element2[int((i//2))])
	a = a+1
	element.append(element3)

	#creating a list of urls of problems
	url = []
	for i in element:
		elem = i.find_element_by_tag_name(("a"))
		url.append(elem.get_attribute("href"))

	#creating a list of the problem's aplbhabetic codes
	codes = []
	for i in element:
		codes.append(i.text)
	if 	x == k:
		a = n%100

	#now iterating every problem one by one and storing the neccessary data
	for j in range(a):
		parent_dir1 = parent_dir + directory + "/"
		subfolder = os.path.join(parent_dir1, codes[j])
		os.mkdir(subfolder)  #creating the respective subfolders of problems
		driver.implicitly_wait(2)
		driver.get(url[j])
		#creating the screenshot of the problem part only and not the whole page
		main = driver.find_element_by_class_name("problem-statement")
		main.screenshot("/Users/aditmalhotra/Documents/" + directory + "/" + codes[j] + "/" + codes[j] + ".png")
		#storing the input and output of sample test runs in the text files
		IO_list = driver.find_elements_by_tag_name("pre")
		for b in range(len(IO_list)):
			if b%2==0:
				fr = open("/Users/aditmalhotra/Documents/" + directory + "/" + codes[j] + "/input" + str(((b)//2)+1) + ".text", "w+" )
				fr.write(IO_list[b].text)
				fr.close()
			else:
				fr = open("/Users/aditmalhotra/Documents/" + directory + "/" + codes[j] + "/output" + str(((b)//2)+1) + ".text", "w+" )
				fr.write(IO_list[b].text)
				fr.close()

driver.quit()



