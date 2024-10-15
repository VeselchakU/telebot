import requests
import time

API_URL = 'https://api.telegram.org/bot'
API_YESNO_URL = 'https://yesno.wtf/api'
BOT_TOKEN = ''
ERROR_TEXT = 'Здесь должна была быть картинка :('

offset = -2
counter = 0
yesno_response: requests.Response
yesno_link: str

while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            yesno_response = requests.get(API_YESNO_URL)
            if yesno_response.status_code == 200:
                yesno_link = yesno_response.json()['image']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={yesno_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
