import time
import pickle
import selenium.webdriver 
import csv

output_file = 'covid-data.csv'
default_timeout = 50


def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title','Address','State','Zipcode','PhoneNumber','Description'])

def add_csv_row(titel, address,state,zipcode, phone,description):
    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([titel, address,state,zipcode, phone,description])

add_csv_head()

driver = selenium.webdriver.Chrome()
driver.get("https://my.castlighthealth.com/corona-virus-testing-sites/")
driver.implicitly_wait(default_timeout)
time.sleep(1)

aa=driver.find_element_by_xpath('//span[@id="select2-state-container"]')
aa.click()
time.sleep(2)
states=driver.find_elements_by_xpath('//li[@aria-selected="false"]')
aa.click()
i=0;
for star in states:
	
	aa=driver.find_element_by_xpath('//span[@id="select2-state-container"]')
	aa.click()

	time.sleep(1)
	state_select=driver.find_elements_by_xpath('//li[@aria-selected="false"]')[i]
	state_select.click()
	time.sleep(2)
	bb=driver.find_element_by_xpath('//span[@id="select2-county-container"]')
	bb.click()
	time.sleep(1)
	county=driver.find_element_by_xpath('//li[@aria-selected="false"]')
	county.click()
	driver.implicitly_wait(8)
	
	time.sleep(9)
	containers=driver.find_elements_by_xpath("//div[@class='result_box']")
	for container in containers:
		title=container.find_element_by_tag_name("h2").text
		
		try:
			address=container.find_elements_by_tag_name("a")[1].text
			adr=address.split(",")

			address3=adr[-1]
			compain=address3.split(" ")
			state=compain[1]
			zipcode=compain[2]
		except:
			address="N/A"
			state="N/A"
			zipcode="N/A"
			

		try:
			phone=container.find_elements_by_tag_name("a")[2].text
		except:
			phone="N/A"

		try:
			description=container.find_element_by_css_selector("p[style='font-size:14px']").text
		except:
			description="N/A"
		
			
			
		add_csv_row(title,address,state,zipcode, phone,description)
		
		
	i+=1
	print(i)

print("done")
