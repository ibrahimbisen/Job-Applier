# Automatic Application Filler

 TL;DR : Overall, this program is designed to save time and effort when applying for jobs on Glassdoor by automating the process of filling out application forms. The program relies on Python Requests, BeautifulSoup4, and Selenium libraries as dependencies.


## Initial Installation
You might have to install pip3 and/or choco in order to install these libraries
```
pip install beautifulsoup4
pip install requests
pip install selenium
```

## How to Run the Scripts and Use Them
(make sure you have python 3 installed not only in your ide but also in Operating System)

Open the command prompt and go to the folder that you are files are located in
Make sure you also have your private information entered into the Applier.py file for it to present your files.

run app_link_scraper.py
```
python3 app_link_scraper.py
```
then hand it the URL for search of the jobs you are looking on Glassdoor that you would like ex:(maybe you are looking for a technical writing internship, search 'technical writer intern' on Glassdoor welcome webpage, either with or without locaiton specified, and feed it to the app_link_scraper.py)
```
Enter URL: 
```
This application scraper will scrape all of the possible easy-apply jobs that are on that webpage and create a carbon copy to scraped_app_links.txt
Then run Applier.py
```
python3 Applier.py
```
This applier will start running through all of the links that are provided and all of you have to do is fallow the instructions

A normal runthough should look like this; 
* install dependencies
* run app_link_scraper.py
* Feed general URL
* Run Applier.py
* Scroll through jobs
* If you like the job description applyif not go to the next job 
<!-- When you run the Applier.py file it will click on the Easy Apply button and start your application, if it can find proper input on the html file of that page it will fill it out, if it does not it will wait for you to go to the next page. It will try to find inputs and files to upload in that page as wel. This action will repeat everytim you go to the next step in the application. If it cannot find any inputs to fill it wont do any actions. When you want to go to the next application you have to come back to the command line and press enter to close the current application tab and open the next application link on a new tab.
I implemented this autofiller this way so that if you see a application with a position that you are not interested in you can directly go to the next application. -->




## Dependencies
-PythonRequests\
-BeautifulSoup4\
-Selenium

## Goals and Current Problems
- Add Autofill Function
- Solve Problems with Selenium 'input' detection
- Add Indeed Scraper
- Add Linkedin Scraper

<!-- 
[Demo]() -->
