import requests
import json

base_url = "https://api.openweathermap.org/data/2.5/weather?"

city = input("Enter a city to get weather details : ")
print("")

api_key = "a49de69b810181cc6659a996563a51dc"

url= base_url + "q=" + city + "&appid=" + api_key
response = requests.get(url)

if response.status_code == 200:
   data = response.json()
   main = data['main']
   temp = main['temp']
   hum = main['humid']
   pres = main['pressure']
   report = data['weather']
   print("Current Weather Condition in ",city,".....")
   print("")
   print("Temperature in (kelvin): ",temp)
   print("Humidity in percent(%): ",hum)
   print("Pressure : ",pres)
   print(f"Weather Report: {report[0]['description']}")
else:
   print("unable to get details .please try again later")
