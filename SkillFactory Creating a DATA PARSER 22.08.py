import requests
from bs4 import BeautifulSoup
import time

import pandas as pd


def collect_user_rates(user_login):
    page_num = 1

    data = []

    session = requests.Session()  # Используем сессию для оптимизации запросов

    while True:



        url = f'https://letterboxd.com/{user_login}/films/diary/page/{page_num}/'
        try:
            response = session.get(url)
            response.raise_for_status()  # Проверяем на ошибки HTTP
        except requests.RequestException as e:
            print(f"Ошибка при запросе {url}: {e}")
            break


        soup = BeautifulSoup(response.text, 'lxml')

        entries = soup.find_all('tr', class_='diary-entry-row viewing-poster-container')


        if not entries:
            break


        for entry in entries:
           time.sleep(0.5)
           # В каждом элементе <tr> ищем элемент <td> с классом 'col-production js-td-production'
           td_film_details = entry.find('td', class_='col-production js-td-production')
           # Теперь, внутри col-production js-td-production ищем элемент <a> и получаем его текстовое содержимое методом .text и удаляем пробелы методом .strip...
           film_name = td_film_details.find('a').text.strip() if td_film_details and td_film_details.find('a') else None

           release_date = entry.find('td', class_='col-releaseyear _aligncenter')



           col_rating = entry.find('td', class_='col-rating _paddinginlinelg')
           rating_span = col_rating.find('span', class_='rating')
           classes = rating_span.get('class', []) if rating_span else []
           rating = classes[1].split('-')[1] if len(classes) > 1 else None

           data.append({'film_name': film_name, 'release_date': release_date, 'rating': rating})

        page_num += 1

        print(f'Собрано данных за {page_num - 1} итеррацию: - {len(data)}')

    return data

user_rates = collect_user_rates(user_login='rfeldman9')
print(f"Общее количество собранных данных: - {len(user_rates)}")

df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')
