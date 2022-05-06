import requests
from bs4 import BeautifulSoup


url = "https://weather.yahoo.co.jp/weather/jp/28/" + str(6310) + ".html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
rs = soup.find(class_='forecastCity')
rs = [i.strip() for i in rs.text.splitlines()]
rs = [i for i in rs if i != ""]
rs_text = rs[0] + "の天気は" + rs[1] + ", 最高気温は" + rs[2] + ", 最低気温は" + rs[3] + ". 明日の天気は" + rs[19] + ", 最高気温は" + rs[20] + ", 最低気温は" + rs[21] + "です。"
# print(rs)
# print(rs[0] + "の天気は" + rs[1] + ", 最高気温は" + rs[2] + ", 最低気温は" + rs[3] + ". 明日の天気は" + rs[19] + ", 最高気温は" + rs[20] + ", 最低気温は" + rs[21] + "です。")

