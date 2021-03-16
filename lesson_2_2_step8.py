from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  

    first_name = browser.find_element_by_css_selector('[name=firstname]').send_keys("First Name")
    last_name = browser.find_element_by_css_selector('[name=lastname]').send_keys("Last Name")
    email = browser.find_element_by_css_selector('[name=email]').send_keys("email@email.com")
    set_file = browser.find_element_by_css_selector('[name=file]').send_keys(file_path)
    submit = browser.find_element_by_css_selector('[type=submit]').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()