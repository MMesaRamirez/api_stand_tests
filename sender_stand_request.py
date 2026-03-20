import configuration
import requests
import data
from data import headers


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_user_path(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        headers=data.headers,json=body
    )

data.user_body['firstName'] = 'M@Fe'
resp = post_user_path(data.user_body)
print(resp.status_code)
print(resp.json())


