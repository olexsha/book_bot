import requests
import time
import json

with open('config.json') as f:
    data = json.load(f)

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = data['bot_token']['token']
offset = -2
timeout = -5
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')