import requests

url = "http://api.openweathermap.org/data/2.5/weather"
config ={
    "id" : 3870011, #temuco
    "appid" :  "Tu api key",
    "lang"  : "es",
    "units" : "metric"
    }

try:
    # respuesta = requests.get( url )
    respuesta = requests.request("GET", url, params = config, timeout = 10  )
    respuesta.raise_for_status() #lanza error si HTTP != 200
    # print( respuesta )
    datos = respuesta.json()
    print( datos )
    clima = datos["weather"][0]["description"]
    clima = clima + " - " + str(datos["main"]["temp"])+"°"
    print(clima)
except requests.exceptions.HTTPError as e:
    print("Error: ", e)