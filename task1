from typing import Any
import requests

PARTNER_TOKEN = ''
LOGIN = ''
PASSWORD = ''


class YClients:
    def __init__(self, partner_token: str):
        self.partner_token = partner_token
        self.user_token = None
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/vnd.yclients.v2+json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.partner_token}'
        })
        self.base_url = 'https://api.yclients.com/api/v1'

    def set_user_token(self, login: str, password: str) -> None:
        url = f'{self.base_url}/auth'
        resp = self.session.post(url, json={"login": login, "password": password}).json()
        self.user_token = resp['data']['user_token']
        self.session.headers.update({
            'Authorization': f'Bearer {self.partner_token}, User {self.user_token}'
        })

    def get_company_id(self) -> int:
        url = f'{self.base_url}/companies?my=1'
        resp = self.session.get(url).json()
        return resp['data'][0]['id']

    def get_client(self, company_id: int, name: str) -> dict[Any]:
        url = f'{self.base_url}/company/{company_id}/clients/search'
        body = {
            "fields": ["id", "name"],
            "filters": [{
                "type": "quick_search",
                "state": {"value": name}
            }]
        }
        resp = self.session.post(url, json=body).json()
        return resp

if __name__ == '__main__':
    yclients = YClients(partner_token=PARTNER_TOKEN)
    yclients.set_user_token(login=LOGIN, password=PASSWORD)
    company_id = yclients.get_company_id()
    result = yclients.get_client(company_id=company_id, name='ivan')

    print(result)
