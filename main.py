#weather app using API
import requests
city = input('Enter the city: ')
country = input('Enter the country: ')
pays = f'{city},{country}'
api_key = 'a755a657573c4b5cb49143655252311' 
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={pays}'

try:
    response = requests.get(url)  
    data = response.json()
    print(data)

    print('WEATHER REPORT')

    location = data['location']['name']
    print(f'The city is: {location}')
    condition = data['current']['condition']['text']

    temperature = data['current']['temp_c']  
    print(f'The temperature is {temperature} degree celsuis')
    if temperature >= 30:
      print('It\'s sunny')
    elif  25 <= temperature < 30:
      print('It\'s warm')
    elif 20 <= temperature < 25:
       print('It\'s mildly sunny')
    elif temperature <= 15:
       print('It\'s cold')
       

    humidity = data['current']['humidity']
    print(f'The humidity status is {humidity} ')
    if humidity >= 80:
       print('It\'s very humid,Most likely to rain')
    elif humidity <= 60 and humidity < 80:
       print('It\'s humid')
    elif humidity <= 30 and humidity < 60:
       print('moderately humid')
    else:
       print('The Air is humid!!')

    windspeed = data['current']['wind_mph']
    print(f'The windspeed is {windspeed} miles per hour')
except:
   print('The country {city} doesn\'t exist')
