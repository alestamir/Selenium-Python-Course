from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12 * math.sin(x))))
  

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    value = calc(x)
    print("calculated value = ", value)
    set_value = browser.find_element_by_id('answer').send_keys(value)
    print("value is set")
    set_checkbox = browser.find_element_by_id('robotCheckbox').click()
    print("checkbox is set")
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_id('robotsRule'))
    print("scrolled to robotsRule")
    set_radiobutton = browser.find_element_by_id('robotsRule').click()
    print("radiobutton is set")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_tag_name('button'))
    #print("scrolled to 'Submit'")
    click_button = browser.find_element_by_tag_name('button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла