from typing import Any
import requests

TOKEN = ''
FIRST_NAME = ''
LAST_NAME = ''

class Megaplan:
    def __init__(self, token: str):
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        })
        self.base_url = 'https://mp82753343.megaplan.ru/api/v3'

    def get_all_humans(self) -> dict[Any]:
        url = f'{self.base_url}/contractorHuman'
        return self.session.get(url).json()

    def create_human(self, first_name, last_name) -> dict[Any]:
        url = f'{self.base_url}/contractorHuman'
        body = {'firstName': first_name, 'lastName': last_name}
        return self.session.post(url, json=body).json()

if __name__ == '__main__':
    megaplan = Megaplan(token=TOKEN)
    megaplan.create_human(first_name=FIRST_NAME, last_name=LAST_NAME)
    users = megaplan.get_all_humans()
    
    print(users)
