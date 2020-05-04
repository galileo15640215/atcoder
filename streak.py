# coding: UTF-8
import datetime
import time
import os

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

user_name = "galileo15640215"
user_url = f"https://kenkoooo.com/atcoder/atcoder-api/results?user={user_name}"
res = requests.get(user_url).json()

# 今の時間(Asia)
now = datetime.datetime.fromtimestamp(time.time(), datetime.timezone(datetime.timedelta(hours=9)))

# 以前に解いたもの
accepted = set()

# 今日のAC
today_accepted = []

# 今日のACチェック
flag = False
ACcnt = 0

# 各提出p を見る
for p in res:

    # pの提出をしたときの時間
    dt = datetime.datetime.fromtimestamp(p['epoch_second'], datetime.timezone(datetime.timedelta(hours=9)))

    # pが解いた問題のID
    p_id = p['problem_id']

    # 正解でないなら関係ない
    if p['result'] != 'AC':
        continue

    # 以前に解いている
    if dt.date() < now.date():
        accepted.add(p_id)

    # 今日解いて、しかもまだ解いていない問題なら
    if dt.date() == now.date() and p_id not in accepted:
        today_accepted.append(p)
        flag = True
        ACcnt += 1

bot = LINENotifyBot(access_token='R1OSwCxEyvJ0tDuSrDOoUwhH1jmrwhnvLjxbLoIahBy')
# test z2JihBz8mPVfAsO3dyqNwfMm8KI2YPlLk0IXYIWQrCu
# true R1OSwCxEyvJ0tDuSrDOoUwhH1jmrwhnvLjxbLoIahBy
if flag:
    bot.send(
        message=user_name+'さんは'+str(ACcnt)+'回ACした！',
        #image='test.png',  # png or jpg
        #sticker_package_id=1,
        #sticker_id=13,
        )
else:
    bot.send(
        message=user_name+'さんはまだ問題を解いていない！',
        #image='test.png',  # png or jpg
        #sticker_package_id=1,
        #sticker_id=13,
        )
