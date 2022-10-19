from rental_back.settings import TELEGRAM_TOKEN
import asyncio
import aiohttp


async def api_call(chat_id, text):
    async with aiohttp.ClientSession() as session:
        token = TELEGRAM_TOKEN
        apiURL = f'https://api.telegram.org/bot{token}/sendMessage'
        async with session.get(apiURL, json={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}) as resp:
            await resp.json()
