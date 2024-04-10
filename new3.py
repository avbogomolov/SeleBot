from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ironchampion.ru")  # Замените ссылку на нужную страницу

# Найдем элемент по id и проскроллим к нему
element = driver.find_element(By.ID, "yandex_rtb_R-A-412676-1")  # Замените "your_element_id" на нужный id элемента
#driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

# Для медленной прокрутки можно использовать цикл, например:
for i in range(1000):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP, Keys.DOWN, Keys.LEFT)

driver.quit()