# import requests
# city_name = 'San Francisco'
# state_code = 'CA'
# country_code = 'US'
# API_key = 'ae0fcc4b9e31df3ec4e039833d6e4ac6' 
# response = requests.get(
#     f"https://api.openweathermap.org/geo/1.0/direct"
#     f"?q={city_name},{state_code},{country_code}"
#     f"&appid={API_key}"
# )
# print(response.text)
# import json
# response_data = json.loads(response.text)
# print(response_date)
# print(response_data[0]['lat'])
# print(response_data[0]['lon'])



# import requests

# city_name = 'San Francisco'
# state_code = 'CA'
# country_code = 'US'
# API_key = 'ae0fcc4b9e31df3ec4e039833d6e4ac6'

# response = requests.get(
#     f"https://api.openweathermap.org/geo/1.0/direct"
#     f"?q={city_name},{state_code},{country_code}"
#     f"&appid={API_key}"
# )

# print(response.text)

# import json
# response_data = json.loads(response.text)   # 原来错在这行：多了 =-

# print(response_data)
# print(response_data[0]['lat'])
# print(response_data[0]['lon'])

# lat = response_data[0]['lat']
# lon = response_data[0]['lon']
# response = requests.get(
#     f"https://api.openweathermap.org/data/2.5/"
#     f"weather?lat={lat}&lon={lon}&appid={API_key}"
# )
# response_data = json.loads(response.text)
# print(response_data)


# response_data['main']['temp']
# print(round(285.44 - 273.15, 1))
# print(round(285.44 * (9 / 5) - 459.67, 1))


BASE = https://www.macroview.club/