import json, requests, sys

url = 'http://t.weather.itboy.net/api/weather/city/101030100'
# print(url)
response = requests.get(url)
response.raise_for_status()
weather_data = json.loads(response.text)
# print(weather_data)
print("鸣谢: ", weather_data['message'])
print("城市: %s, 时间: %s" % (weather_data['cityInfo']['city'], weather_data['time']))
print("湿度: %s, pm25: %s, pm10: %s, 空气质量: %s, 温度: %s, 提示: %s" %( weather_data['data']['shidu'], weather_data['data']['pm25'], weather_data['data']['pm10'], weather_data['data']['quality'], weather_data['data']['wendu'], weather_data['data']['ganmao'] ))

