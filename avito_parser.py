import requests
from bs4 import BeautifulSoup


def scrape_avito_rental_prices(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    studio_ads = soup.select('.item.js-item-serp-card__link')
    prices = []

    for ad in studio_ads:
        link = ad['href']

        ad_response = requests.get(link, headers=headers)
        ad_soup = BeautifulSoup(ad_response.content, 'html.parser')

        
        price_element = ad_soup.select_one('.price')
        if price_element:
            price_text = price_element.text.strip()
            # Извлекаем числовую часть цены
            price = ''.join(filter(str.isdigit, price_text))
            prices.append(price)
        else:
            prices.append(None)

    return prices


