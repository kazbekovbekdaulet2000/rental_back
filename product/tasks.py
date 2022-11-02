from celery import shared_task
from rental_back.settings import TELEGRAM_TOKEN, TELEGRAM_TOKEN_RESERVE
import requests


@shared_task(time_limit=3600)
def send_telegram_message(chat_id, text):
    token = TELEGRAM_TOKEN
    tokenReserve = TELEGRAM_TOKEN_RESERVE
    apiURL = f'https://api.telegram.org/bot{token}/sendMessage'
    apiURLReserve = f'https://api.telegram.org/bot{tokenReserve}/sendMessage'
    req = requests.get(apiURL, params={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'})
    if (req.status_code != 200):
        reqReserve = requests.get(apiURLReserve, params={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'})
        return reqReserve.status_code
    return req.status_code
