import aiohttp
import asyncio
import json

from tgbot.config import load_config


async def get_currency(rate1, rate2, summ):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://www.cbr-xml-daily.ru/latest.js') as resp:
            responce = await resp.read()
        data = json.loads(responce)
        if rate1 != 'RUB':
            course1 = float(data['rates'][rate1])
        else:
            course1 = 1
        if rate2 != 'RUB':
            course2 = float(data['rates'][rate2])
        else:
            course2 = 1

        result = summ * (course2 / course1)

        return round(result, 2)



#
# asyncio.run(get_currency('EUR', 'RUB', 100))



