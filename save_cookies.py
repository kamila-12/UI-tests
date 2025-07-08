from selenium import webdriver
import pickle
import time

driver = webdriver.Chrome()
driver.get("https://market.o.kg/")

print("Sign in with Google")
time.sleep(60)

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
print("Cookies is saved in cookies.pkl")
driver.quit()