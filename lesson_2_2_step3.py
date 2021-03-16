from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    input1 = int(browser.find_element_by_id('num1').text)
    input2 = int(browser.find_element_by_id('num2').text)
    value = str(input1 + input2)
    print("calculated value = ", value)
    
    select = Select(browser.find_element_by_tag_name("select")) # создаем обжект со всеми значениями списка
    select.select_by_value(value) # ищем элемент со значением value
    click_button = browser.find_element_by_tag_name('button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла