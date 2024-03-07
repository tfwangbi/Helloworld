import requests
from bs4 import BeautifulSoup

URL = 'https://movie.douban.com/top250'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}



movie_titles = []

for num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={num}", headers=headers)
    if response.ok:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all_titles = soup.findAll('span', attrs = {'class':'title'})

        for title in all_titles:
            # print(title.string)
            title_string = title.string
            if "/" not in title_string:
                # print(title_string)
                movie_titles.append(title_string)


    else:
        print("Request fail.....")

print(movie_titles)