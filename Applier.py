import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# These two lines are to set up options 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 
# open new Chrome window
driver = webdriver.Chrome()

#---------------------------------------------------------------------------
# Personal Information 
first_name = ""
last_name = ""
email = ""
cover_letter = ""
phone_number = ""
address = ""
headline = ""

class education(object):
	name = ""
	degree = ""
	major = ""
	start_month = ""
	start_day = ""
	start_year = ""
	end_month = ""
	end_day = ""
	end_year = ""
	def __init__(self, name, degree, major, start_month,
	      		start_day, start_year, end_month, end_day, end_year):
		self.name = name
		self.degree = degree
		self.major = major
		self.start_month = start_month
		self.start_day = start_day
		self.start_year = start_year
		self.end_month = end_month
		self.end_day = end_day
		self.end_year = end_year

# Example
my_school = education('University', 'Bachelors', 'Engineering',0,0,0,0,0,0)

class job(object):
	title = ""
	company = ""
	industry = ""
	summary = ""
	currently_work_here = False
	start_month = ""
	start_day = ""
	start_year = ""
	end_month = ""
	end_day = ""
	end_year = ""
	def __init__(self, title, company, industry, summary, currently_work_here,
				start_month, start_day, start_year,
				end_month, end_day, end_year):
		self.title = title
		self.company = company
		self.industry = industry
		self.summary = summary
		self.currently_work_here = currently_work_here
		self.start_month = start_month
		self.start_day = start_day
		self.start_year = start_year
		self.end_month = end_month
		self.end_day = end_day
		self.end_year = end_year
# Example
job1 = job("Title", "Glassdoor", "Cybersecurity", "blah blah blah blah", True, "June", "1", "1998", "N/A", "N/A", "N/A")

relevantExperienceTitle = job1.title
relevantExperienceCompany = job1.company

# End of Personal Information
# --------------------------------------------------------------------------


# This function takes a file that the app finder 
def extract_links(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    links = [line.strip() for line in lines if line.startswith('http')]
    return links

def open_webpage_chrome(links):

    for link in links:
        # go to the first link
        driver.get(link)  
        # Timer for waiting webpage to load
        time.sleep(0.1)
        
        # checks if you want to apply to this job specidically
        if input("Do you want to apply if yes type'yes' else type anything else.") == 'yes':
            button_xpath = '//*[@id="PageContent"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/button'
            button = driver.find_element(By.XPATH, button_xpath)
            button.click()
        else:
             continue


# The commented sections are for Future Autofilling Improvements
		# Loop for autofilling or going to the next application
       
        # asking_for_a = input("Enter 'yes' if you want to autofill otherwise press Enter to open the next Job Application, or Ctrl+C to exit...")
        # check_if_want_autofill_again = 'no'
        # if  asking_for_a == 'yes':
        #     auto_filler()
        #     print("autofilled   1     ")
        #     while check_if_want_autofill_again == 'yes':
        #         auto_filler()
        #         print("autofilled   2     ")
        #         check_if_want_autofill_again = input("If you would like to try to autofill again please type'yes', or Ctrl+C to exit...")
        # else:
        #     # This part of the code is supposed to close the tab if another tab is opened when pressed easy apply button
		# 	# due to complication in the code and limited knowledge of the selenium framework couldnt get it to work
		# 	# so will have to manually close 
        #     next_job = input("When you want to go to the next job please press Enter")
        #     continue
                  


# def auto_filler():
#     try:
#          print(" filled as much as possible")
#     except:
#          print('Could not fill anything')
    

def main():
    file_name = 'scraped_app_links.txt'
    links = extract_links(file_name)
    open_webpage_chrome(links)

if __name__ == "__main__":
    main()