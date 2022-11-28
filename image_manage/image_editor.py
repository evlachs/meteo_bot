from PIL import Image, ImageDraw, ImageFont


class ImageEditor:

    def __init__(self, daytime: str):
        if daytime == 'n':
            self.image = Image.open('data/pics/night.png')
        else:
            self.image = Image.open('data/pics/day.png')
        self.draw = ImageDraw.Draw(self.image)

    def paste_time(self, time: str) -> None:
        font = ImageFont.truetype('arialbd.ttf', size=68)
        self.draw.text((50, 53), time, font=font)

    def paste_pressure(self, pressure: str):
        font = ImageFont.truetype('arialbd.ttf', size=68)
        self.draw.text((368, 735), pressure, font=font)

    def paste_temp(self, temp: str, feels_like: str):
        temp_font = ImageFont.truetype('arialbd.ttf', size=68)
        fl_font = ImageFont.truetype('arial.ttf', size=40)
        self.draw.text((346, 383), temp, font=temp_font)
        self.draw.text((639, 483), feels_like, font=fl_font, fill='#CBCBCB')

    def paste_humidity(self, humidity: str):
        font = ImageFont.truetype('arialbd.ttf', size=68)
        self.draw.text((368, 610), humidity, font=font)

    def paste_wind(self, wind: str):
        font = ImageFont.truetype('arialbd.ttf', size=68)
        self.draw.text((368, 861), wind, font=font)

    def paste_icon(self, path):
        icon = Image.open(path)
        self.image.alpha_composite(icon, dest=(487, 338))

    def save_image(self) -> None:
        self.image.save('data/pics/post.png')
