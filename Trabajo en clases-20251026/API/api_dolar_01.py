import requests

url = "https://open.er-api.com/v6/latest/USD"
try:
    respuesta = requests.get( url )
    respuesta.raise_for_status() #lanza error si HTTP != 200
    # print( respuesta )
    datos = respuesta.json()
    print("ultima actualiz.:",datos.get("time_last_update_utc"))
    print("sigte. actualiz.:",datos.get("time_next_update_utc"))
    # print( datos )
    valor_clp = datos["rates"]["CLP"]
    print(valor_clp)
except requests.exceptions.HTTPError as e:
    print("Error: ", e)