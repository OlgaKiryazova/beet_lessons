import json
from pprint import pprint

from requests import Session
from bs4 import BeautifulSoup


def get_response(url):
    with Session() as session:

        response = session.get(url, timeout=10)

        assert response.status_code == 200, 'Bad response'
        print(response.status_code)

    return response


def html_parser(response):
    soup = BeautifulSoup(response.content, 'html.parser')


    items_list = soup.select('rz-catalog-tile', class_='ng-star-inserted')

    data_list = []

    for item in items_list:
        name = item.select('.goods-tile__title')[0].text.strip()
        price = item.select('p span', class_='goods-tile__price-value')[0].text.replace('\xa0', '')
        reviews = item.select('.goods-tile__reviews-link')[0].text.strip()
        img_url1 = item.select('img', class_='goods-tile__picture ng-star-inserted')[0]['src']


        data_list.append(
                {'name': name,
                 'price': price,
                 'reviews': reviews,
                 'img_url1': img_url1,

                 })

    print(len(data_list))
    return data_list


def json_file_writer(data, indent=4):
    with open('rozetka.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=indent)


def main():

    url = 'https://rozetka.com.ua/ua/notebooks/c80004/'

    response = get_response(url)

    data = html_parser(response)

    json_file_writer(data)
    pprint(data)


if __name__ == '__main__':
    main()
