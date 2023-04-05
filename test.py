import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')

latitude = []
longitude = []

def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y
    except:
        return[0,0]


csv = pd.read_csv('서울시 공영주차장 안내 정보.csv', encoding='cp949')
print(csv.head())

address = csv['주소']
print(address.head())

for i in range(len(address)):
    a = address[i].split(' ')
    address[i] =  " ".join(a[0:4])

for i in address:
    latitude.append(geocoding(i)[0])
    longitude.append(geocoding(i)[1])

address_df = pd.DataFrame({'주차장명':csv['주차장명'], '상세주소':csv['주소'], '위도':latitude, '경도':longitude})
print(address_df.head())