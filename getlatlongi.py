from geopy.geocoders import Nominatim


def findlatlon(name):
    geolocator = Nominatim(user_agent="Arth's_app")
    location = geolocator.geocode(name)
    print(location.address)
    return (location.latitude, location.longitude)
