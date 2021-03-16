from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(x))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    wait_button = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100' )
    )
    click_button = browser.find_element(By.ID, "book").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "solve"))
    x = int(browser.find_element(By.ID, "input_value").text)
    value = calc(x)
    set_value = browser.find_element(By.ID, "answer").send_keys(value)
    click_submit = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(10)
    browser.quit()