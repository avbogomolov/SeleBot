from bs4 import BeautifulSoup
import requests
import random

# URL страницы, с которой вы хотите получить ссылки
url = 'https://ironchampion.ru' # Замените на URL вашей страницы

# Загружаем содержимое страницы
response = requests.get(url)

# Парсим HTML содержимое
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки на странице
links = soup.find_all('a', href=True)

# Рандомно выбираем одну из ссылок
random_link = random.choice(links)

# Выводим выбранную ссылку
print(random_link['href'])