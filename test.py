from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Quickstartのサンプルはカレンダー参照用で、カレンダーに書き込むにはSCOPESを変更する
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
# 認証キーのファイル名
CLIENT_SECRET_FILE = 'client_secret.json'
# アプリケーション名（任意）
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
 
    # 以降Quickstartから変更
     
    # 図書館カレンダーをスクレイピングして休館日を取得
    # 当月と翌月の2ヶ月分あるが、翌月のカレンダーのみ取得する
    url = "http://www.ndl.go.jp/jp/service/tokyo/time.html"
    html_data = urlopen(url).read()
    html_parsed = BeautifulSoup(html_data, "html.parser")
 
    calendar = html_parsed.findAll("table", class_="calendarTable")[1]
 
    # 年と月のリスト
    yearmonth = re.findall('\d+', calendar.caption.text)
 
    # 休館日を取得
    holidays = calendar.findAll("td", class_="holiday")
    days = []
    for holiday in holidays:
        days.append(holiday.text.strip('()'))
 
 
    # Googleカレンダーに休館日を登録
    for day in days:
        # Googleカレンダーに登録する日付（YYYY-MM-DD）を作成
        date = "{}-{:0>2}-{:0>2}".format(yearmonth[0], yearmonth[1], day)
 
        # 休館日を終日イベントとして登録するように設定
        event = {
            'summary': '国会図書館休館日',
            'description': '国会図書館の休館日',
            'start': {
                'date': date,
                'timeZone': 'Asia/Tokyo',
            },
            'end': {
                'date': date,
                'timeZone': 'Asia/Tokyo',
            },
        }
 
        # 休館日を登録するGoogleカレンダーIDをcalendarIdに指定し、イベントを登録する
        event = service.events().insert(calendarId='calendarId.calendar.google.com', body=event).execute()

if __name__ == '__main__':
    main()