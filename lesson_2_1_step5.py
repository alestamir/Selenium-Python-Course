from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    print("calculated value = ", y)
    set_value = browser.find_element_by_id('answer').send_keys(y)
    set_check_box = browser.find_element_by_id('robotCheckbox').click()
    set_radiobutton = browser.find_element_by_id('robotsRule').click()
    click_button = browser.find_element_by_tag_name('button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла