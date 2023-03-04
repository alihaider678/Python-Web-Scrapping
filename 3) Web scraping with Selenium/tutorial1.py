# Selenium Tutorial #1
 

from selenium import webdriver

# Set path of chromedriver
path = "C:\Program Files (x86)\chromedriver.exe"

# Create a new Chrome browser instance
driver = webdriver.Chrome(path)

# Navigate to the website
driver.get("https://techwithtim.net")

# Get the website title
print(driver.title)

# Close the browser window
driver.quit()

