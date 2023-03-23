from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
driver.get("https://www.google.com")
sleep(5)
input = driver.find_element(By.NAME, "q")
input.send_keys("kodlama io")
searcButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searcButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlama io sitesinde su anda {len(listOfCourses)} adet kurs var.")

# sleep(10)
while True:
    continue # sonsuz bir dongu yaratildigi icin uygulama kapanmayacak.

# HTML LOCATORS

# Full XPath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a

# XPath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a

# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a