import pandas as pd
from geopy.geocoders import Nominatim

df = pd.read_csv('data-1677295003089.csv') #caminho do arquivo CSV

geolocator = Nominatim(user_agent='myapplication') #limitador

def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        return location.latitude, location.longitude
    except:
        return 'Endereço não encontrado', 'Endereço não encontrado'


df['lat'], df['long'] = zip(*df['endereco'].apply(get_coordinates)) #adicionar nova coluna
df.to_csv('arquivo_com_coordenadas.csv', index=False)   #gerar novo arquivo