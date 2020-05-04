import requests


class LINENotifyBot:
    API_URL = 'https://notify-api.line.me/api/notify'
    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
            self, message,
            image=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            )

bot = LINENotifyBot(access_token='z2JihBz8mPVfAsO3dyqNwfMm8KI2YPlLk0IXYIWQrCu')

bot.send(
    message='Write Your Message',
    #image='test.png',  # png or jpg
    #sticker_package_id=1,
    #sticker_id=13,
    )