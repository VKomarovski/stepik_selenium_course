import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222") 

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    #browser.implicitly_wait(12)
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = browser.find_element_by_id('book')
    button1.click()

    #time.sleep(2)
    #alert = browser.switch_to.alert
    #alert.accept()

    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

    #time.sleep(1)
    #first_elem = browser.find_element_by_id('num1')
    #first_numb = first_elem.text
    #print(first_numb)
    #print(type(first_numb))
    #second_elem = browser.find_element_by_id('num2')
    #second_numb = second_elem.text
    #sum = str(int(first_numb) + int(second_numb))

    #select = Select(browser.find_element_by_tag_name('select'))
    #select.select_by_value(sum)
    x_elem = browser.find_element_by_id('input_value')
    x = x_elem.text
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))
#    option2 = browser.find_element_by_id('robotCheckbox')
#    option2.click()
#    option3 = browser.find_element_by_id('robotsRule')
#    option3.click()


    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
