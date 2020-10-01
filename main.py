import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    descrs = soup.find('ul', attrs={'class': 'list-unstyled'})

    links = []

    for i in descrs:
        a = soup.find('a').get('href')
        links.append(a)

    return links


def main():
    url = 'https://retailer.ru/news/'
    all_links = get_all_links(get_html(url))
    for k in all_links:
        print(k)


if __name__ == '__main__':
    main()
