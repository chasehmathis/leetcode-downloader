import requests
from bs4 import BeautifulSoup
import json
import os

data_path = "problem"
def fetch_one_question(slug, num):

    webpage = requests.get(f'https://leetcode.com/problems/{slug}/')
    soup = BeautifulSoup(webpage.content, 'html.parser')

    script_tag = soup.find('script', {'id': '__NEXT_DATA__', 'type': 'application/json'})

    json_data = json.loads(script_tag.string)
    soup2 = BeautifulSoup(json_data['props']['pageProps']['dehydratedState']['queries'][6]['state']['data']['question']['content'], 'html.parser')

    with open(f"{data_path}/{num}-{slug}.txt", 'w') as f:
        f.write(soup2.text)


def main():

    for problem in os.listdir('./submission'):
        num = problem[:4]
        slug = '-'.join(problem.split('-')[1:])
        slug = slug[:-3]

        fetch_one_question(slug, num)

if __name__ == '__main__':
    main()