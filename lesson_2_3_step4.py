from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    journey_click = browser.find_element_by_css_selector('div > button').click()
    confirm_alert1 = browser.switch_to.alert.accept()
    x = int(browser.find_element_by_id('input_value').text)
    value = calc(x)
    set_value = browser.find_element_by_id('answer').send_keys(value)
    click_submit = browser.find_element_by_css_selector('[type=submit]').click()
   
    alert_value = browser.switch_to.alert.text.split(': ')[-1]
    print(alert_value)
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()