import requests
from bs4 import BeautifulSoup


def scrape_avito_rental_prices(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим все объявления о студиях в Даниловском районе
    studio_ads = soup.select('.item.js-item-serp-card__link')
    prices = []

    for ad in studio_ads:
        # Получаем ссылку на объявление
        link = ad['href']

        # Отправляем запрос на страницу объявления
        ad_response = requests.get(link, headers=headers)
        ad_soup = BeautifulSoup(ad_response.content, 'html.parser')

        # Находим цену аренды на странице объявления
        price_element = ad_soup.select_one('.price')
        if price_element:
            price_text = price_element.text.strip()
            # Извлекаем числовую часть цены
            price = ''.join(filter(str.isdigit, price_text))
            prices.append(price)
        else:
            prices.append(None)

    return prices


# Пример использования
url = 'https://www.avito.ru/all/kvartiry/sdam/na_dlitelnyy_srok/studii-ASgBAQICAkSSA8gQ8AeQUgFAzAgUjFk?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYytlLKTSxQsq4FBAAA__8Xe4TEHwAAAA&map=eyJzZWFyY2hBcmVhIjp7ImxhdEJvdHRvbSI6NTUuNjg5NDM0MTI4Mzg0MjE0LCJsYXRUb3AiOjU1LjcyNDYzOTU2NDkyNjk3NCwibG9uTGVmdCI6MzcuNTc1NjgwNjE4Mjg2MDg2LCJsb25SaWdodCI6MzcuNjk3MjE2ODczMTY4OTA1fSwiem9vbSI6MTR9'  # Пример URL, нужно заменить на актуальный
prices = scrape_avito_rental_prices(url)
for i, price in enumerate(prices):
    print(f"Цена {i + 1}-й студии: {price} руб.")
