import requests # url:get요청
import csv # csv로 저장
import os # 폴더 생성
from datetime import datetime # 시간 변환

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
city = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
response = requests.get(url)
result = response.json()
result
humid = result["main"]["humidity"] # 습도
temp = result["main"]["temp"] # 현재 기온
weather = result["weather"][0]["main"] #현재 날씨 상태
current_time = datetime.now().strftime("%H시 %M분 %S초")

# csv
header = ["current_time", "weather", "temp", "humid"]

# 만약, seoul_weather.csv 없으면 만들고 있으면 덮어쓰기
csv_exist = os.path.exists("seoul_weather.csv")
with open("seoul_weather.csv","a")as file:
    writer = csv.writer(file)

    if not csv_exist:
        writer.writerow(header)
    writer.writerow([current_time, weather, temp, humid])
    print("서울 기온 저장 완료")
    
