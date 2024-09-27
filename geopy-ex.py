from geopy.geocoders import Nominatim
#Especificar un User-Agent personalizado
geolocator = Nominatim (user_agent="my_geocoder")
try:
    location = geolocator.geocode ("1600 Amphitheatre Parkway, Mountain View, CA") 
    if location:
        print(location.address)
        print((location.latitude, location.longitude))
    else:
        print("No se encontró la ubicación.")
except Exception as e:
    print (f"Ocurrió un error: {e}")