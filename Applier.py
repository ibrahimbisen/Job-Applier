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

# #---------------------------------------------------------------------------
# # Personal Information 
# first_name = ""
# last_name = ""
# email = ""
# cover_letter = ""
# phone_number = ""
# address = ""
# headline = ""

# class education(object):
# 	name = ""
# 	degree = ""
# 	major = ""
# 	start_month = ""
# 	start_day = ""
# 	start_year = ""
# 	end_month = ""
# 	end_day = ""
# 	end_year = ""
# 	def __init__(self, name, degree, major, start_month,
# 	      		start_day, start_year, end_month, end_day, end_year):
# 		self.name = name
# 		self.degree = degree
# 		self.major = major
# 		self.start_month = start_month
# 		self.start_day = start_day
# 		self.start_year = start_year
# 		self.end_month = end_month
# 		self.end_day = end_day
# 		self.end_year = end_year

# # Example
# my_school = education('University', 'Bachelors', 'Engineering',0,0,0,0,0,0)

# class job(object):
# 	title = ""
# 	company = ""
# 	industry = ""
# 	summary = ""
# 	currently_work_here = False
# 	start_month = ""
# 	start_day = ""
# 	start_year = ""
# 	end_month = ""
# 	end_day = ""
# 	end_year = ""
# 	def __init__(self, title, company, industry, summary, currently_work_here,
# 				start_month, start_day, start_year,
# 				end_month, end_day, end_year):
# 		self.title = title
# 		self.company = company
# 		self.industry = industry
# 		self.summary = summary
# 		self.currently_work_here = currently_work_here
# 		self.start_month = start_month
# 		self.start_day = start_day
# 		self.start_year = start_year
# 		self.end_month = end_month
# 		self.end_day = end_day
# 		self.end_year = end_year
# # Example
# job1 = job("Title", "Glassdoor", "Cybersecurity", "blah blah blah blah", True, "June", "1", "1998", "N/A", "N/A", "N/A")

# relevantExperienceTitle = job1.title
# relevantExperienceCompany = job1.company

# # End of Personal Information
# # --------------------------------------------------------------------------


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


		# # The commented sections are for Future Autofilling Improvements
		# # Loop for autofilling or going to the next application
       
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
                  


def auto_filler():
    try:
        #  forstnameweb = driver.find_element(By.ID,'//*[@id="input-firstName"]')
        #  forstnameweb.send_keys(first_name)
         
        # #  forstnamepopup = driver.find_element(By.ID,'//*[@id="input-applicant.name"]')
        # #  forstnamepopup.send_keys(first_name)
         print("filled as much as possible")
    except Exception as error:
         print(error)
         print('Could not fill anything')
    
# 
# 
# PHONE CALL
# 
# 


# #################################################
# #################################################
# #################################################
# #################################################
# #################################################
# #################################################
# #################################################
			# PERSONAL INFORMATION
	
first_name = "Ibrahim"
last_name = "Bisen"
email = "Ebisen2003@gmail.com"
cover_letter = "Dear Hiring Manager, I am writing to express my interest in the aerospace and \
	robotics engineering internship at your esteemed company. I am currently a junior pursuing a \
	Bachelor of Science in Aerospace Engineering with a minor in Computer Science at the University \
	of Texas at Austin, set to graduate in Fall 2025. My hands-on experience with relevant projects \
	and internships has equipped me with a solid foundation in both fields. I am eager to leverage my\
	  skills to contribute to your team and further enhance my expertise in engineering and software \
	development. Since high school, I have been passionate about model rocketry and have diligently\
	  worked towards obtaining my Level 2 certification in high-power rocketry. My academic coursework, \
	coupled with practical experience, has provided me with a comprehensive understanding of this field. \
	I have successfully completed projects such as creating a 5-foot-long, 4-inch diameter fiberglass and \
	carbon fiber composite body tube and designing a reaction wheel using a BLDC motor. I developed the reaction \
	wheel using 3D printing, CNC machining, and C++ programming, which takes real-time input from a 9-DOF IMU to \
	stabilize the rocket for video recording. In the past year, I have dedicated myself to developing a humanoid \
	quadruped robot named Gray. This project has allowed me to hone my skills in designing lightweight and efficient\
	  SolidWorks and CAD models while mastering the manufacturing process with 3D FDM and SLA printers to achieve \
	maximum durability and strength. My ultimate goal is to enable Gray to walk autonomously using a machine \
	learning algorithm, which I am currently integrating into the robot. My commitment to learning\
	  CAD design and software engineering with Python, MATLAB, C++, HTML, CSS, and JavaScript has\
	  been both challenging and rewarding. Thank you for taking the time to consider my application. \
	I am grateful for the opportunity to potentially join your team and contribute to the exciting \
	projects at your company. I am confident that my background and passion for aerospace and \
	robotics engineering make me a strong candidate for this internship. Sincerely, \
	Ibrahim Bisen"
phone_number = "5127485271"
address = "908 inge lane, Leander, Texas, 78641"
headline = "Engineering Student"

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

my_school = education('University of Texas at Austin', 'Bachelors of Science', 'Aerospace Engineering and Computer Science',
		      7,18,2021,5,2,2024)

num_of_jobs = 5
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

# Example:  job1 = job("Title", "Glassdoor", "Cybersecurity", "blah blah blah blah", True, "June", "1", "1998", "N/A", "N/A", "N/A")
job1 = job('R&D Engineering Intern', 'Terra Pave International', 'Enviromental Engineering','Research and develop \
	   real-life implementation of Terra Fog™ to enhance asphalt pavement by preventing oxidation, renewing appearance,\
	    sealing cracks, and strengthening the structural matrix as an R&D Engineering Intern.', True, 7, 1, 2022, "N/A", 
		"N/A","N/A" )
job2 = job('Track Design and Manufacturing Engineer', 'Texas Guadaloop', 'Engineering','Designed and stress-tested CAD \
	   designs and GD&T drawings for a custom hyperloop track. Manufactured 6 feet of track for testing, demonstrating \
	   proficiency in executing complex manufacturing processes with precision. Collaborated effectively with the Track\
	    and Manufacturing Teams to optimize performance and efficiency in a fast-paced Hyperloop Development.', True,
		1,1,2023,'N/A','N/A','N/A')
job3 = job('Data Analyst','University of Texas at Austin','Data Analysis','Data analyst and evaluator for a CCBHC-E\
	    grant from SAMHSA awarded to a local mental health authority. Developed an advanced Python algorithm using \
	   Pandas to analyze and build a comprehensive database. Increased efficiency and accuracy in data management and \
	   analysis through algorithm implementation.', False, 8,1,2022,11,30,2022)
job4 = job('Machine Shop Associate', 'University of Texas at Austin', 'Manufacturing', 'Designed CAD models and manufactured\
	    metal parts for academic and non-academic projects with precision and attention to detail. Created injection mold \
	   plates for fidget spinners using SolidWorks and Fusion 360 and manufactured them in HAAS CNC machine. Mastered the use \
	   of various machine tools, such as band saw, lathe, milling machine, automatic milling machine, and bench grinder, \
	   enhancing proficiency in metalworking and manufacturing.', False, 9,1,2021,4,1,2022)
job5 = job('Intern','Rice University', 'AI and Education', 'Published five articles with IGI Global Academic Journals,\
	    contributing to academic discourse on the role of AI and machine learning in higher education. Presented research \
	   at London International Conferences and provided valuable insights and recommendations for leveraging these\
	    technologies to enhance the teaching and learning experience. Led four different groups of students in organizing \
	   and writing these articles, helping to develop their research and writing skills while contributing to academic \
	   discourse. Researched US government STEM opportunities for Rice University`s STEM Programs Director and presented\
	    valuable insights and strategies for advancing the university`s initiatives.',False,5,1,2020,1,30,2022)


	
# #################################################
# #################################################
# #################################################
# #################################################
# #################################################
# #################################################
# #################################################

def main():
    file_name = 'scraped_app_links.txt'
    links = extract_links(file_name)
    open_webpage_chrome(links)

if __name__ == "__main__":
    main()