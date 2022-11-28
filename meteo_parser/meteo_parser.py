import requests
from datetime import datetime
from cairosvg import svg2png

from conf import Y_API


class Weather:
    """"""
    url = 'https://api.weather.yandex.ru/v2/informers?lat={0}&lon={1}'
    headers = {'X-Yandex-API-Key': Y_API}

    def __init__(self, lat: float, lon: float):
        self._r = requests.request('GET', self.url.format(lat, lon), headers=self.headers)
        self.weather_json = self._r.json()

    @property
    def temp(self) -> str:
        return str(self.weather_json['fact']['temp'])

    @property
    def feels_like(self) -> str:
        return str(self.weather_json['fact']['feels_like'])

    @property
    def wind(self) -> str:
        return str(self.weather_json['fact']['wind_speed'])

    @property
    def humidity(self) -> str:
        return str(self.weather_json['fact']['humidity'])

    @property
    def pressure(self) -> str:
        return str(self.weather_json['fact']['pressure_mm'])

    @property
    def daytime(self) -> str:
        return self.weather_json['fact']['daytime']

    @property
    def time(self) -> str:
        return datetime.now().strftime('%H:%M')

    def icon(self) -> str:
        path = 'data/pics/icon.png'
        icon_id = self.weather_json['fact']['icon']
        icon_url = f'https://yastatic.net/weather/i/icons/funky/dark/{icon_id}.svg'
        svg2png(url=icon_url, write_to=path, dpi=300, scale=7)
        return path
