import csv
import requests
from bs4 import BeautifulSoup

r = requests.get("https://atcoder.jp/home")
soup = BeautifulSoup(r.content, "html.parser")
time = soup.find_all("time", class_="fixtime fixtime-short")
contest = soup.find_all("small")
times = []
for i in time:
    times.append(i.getText())
print(times)
contests = [] 
for i in contest:
    contests.append(i.getText())
out = []
for i in range(len(contests)):
    if contests[i][0:2] == "20":
        pass
    elif contests[i][0:4] == "◉ pr":
        pass
    elif contests[i][0:4] == "post":
        pass
    elif contests[i][0:4] == "last":
        pass
    elif contests[i][0:4] == "Copy":
        pass
    else:
        out.append(contests[i])
print(out)
print(len(times))
print(len(out))