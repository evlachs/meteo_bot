import asyncio
import time
from datetime import datetime

from loader import bot
from image_manage import ImageEditor
from meteo_parser import Weather
from conf import CITY_COORD, LAUNCH_TIMES, CHANNEL
from csv_manage import SheetManager
from messages import MESSAGES


async def send_message(delay):
    while True:
        now = datetime.now().strftime('%H:%M')
        w_day = datetime.today().weekday()
        if now in LAUNCH_TIMES:
            weather = Weather(CITY_COORD['latitude'], CITY_COORD['longitude'])
            today = datetime.today().strftime('%d.%m.%Y')
            ie = ImageEditor(weather.daytime)
            ie.paste_time(weather.time)
            ie.paste_humidity(weather.humidity)
            ie.paste_temp(weather.temp, weather.feels_like)
            ie.paste_pressure(weather.pressure)
            ie.paste_wind(weather.wind)
            ie.paste_icon(weather.icon())
            ie.save_image()
            sm = SheetManager()
            c = sm.get_value(int(weather.temp), round(float(weather.wind)))
            if w_day == 6:
                await bot.send_photo(CHANNEL, photo=open('data/pics/post.png', 'rb'))
                return
            if isinstance(c, str) and now == LAUNCH_TIMES[0]:
                await bot.send_photo(CHANNEL, photo=open('data/pics/post.png', 'rb'),
                                     caption=MESSAGES['active_day'].format(today, c))
            elif isinstance(c, str) and now == LAUNCH_TIMES[1]:
                await bot.send_photo(CHANNEL, photo=open('data/pics/post.png', 'rb'),
                                     caption=MESSAGES['active_evening'].format(today, c))
            elif not c and now == LAUNCH_TIMES[0]:
                await bot.send_photo(CHANNEL, photo=open('data/pics/post.png', 'rb'),
                                     caption=MESSAGES['not_active_day'].format(today))
            elif not c and now == LAUNCH_TIMES[1]:
                await bot.send_photo(CHANNEL, photo=open('data/pics/post.png', 'rb'),
                                     caption=MESSAGES['not_active_evening'].format(today))
        await asyncio.sleep(delay)
