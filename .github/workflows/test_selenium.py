from selenium import webdriver
import time

# Initialize Safari WebDriver
driver = webdriver.Safari()

# Open a website
driver.get("https://jordy-zone.streamlit.app")
time.sleep(20)


# Print the page title
print(driver.title)

# Close the browser
driver.quit()
