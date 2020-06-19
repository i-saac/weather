from bs4 import BeautifulSoup
import geopy
import requests


class Scraper:

    def __init__(self, address):
        # initialize geolocator
        geolocator = geopy.Nominatim(user_agent='my-application')

        # initialize address
        self.address = address

        # determine if address is valid
        if self.is_valid_address(geolocator):
            # if address is valid get lat/long
            self.location = geolocator.geocode(self.address, country_codes=['US'])
            self.latitude = self.location.latitude
            self.longitude = self.location.longitude
        else:
            # otherwise set both to 0 to purposefully throw invalid address
            self.latitude = 0
            self.longitude = 0

        # set up soup scraper
        self.url = f'https://forecast.weather.gov/MapClick.php?lat={self.latitude}&lon={self.longitude}'
        self.source = requests.get(self.url).text
        self.soup = BeautifulSoup(self.source, 'lxml')

    # retrieve location
    def get_location(self):
        try:
            location = self.soup.find('h2', class_='panel-title').text
            return location
        except AttributeError:
            return 'Error: Invalid Address'

    # retrieve forecast
    def get_forecast(self):
        try:
            forecast = self.soup.find('p', class_='myforecast-current').text
            return forecast
        except AttributeError:
            return 'Error: Invalid Address'

    # retrieve temperature in fahrenheit
    def get_temp_f(self):
        try:
            temp_f = self.soup.find('p', class_='myforecast-current-lrg').text
            return temp_f
        except AttributeError:
            return 'Error: Invalid Address'

    # retrieve temperature in celsius
    def get_temp_c(self):
        try:
            temp_c = self.soup.find('p', class_='myforecast-current-sm').text
            return temp_c
        except AttributeError:
            return 'Error: Invalid Address'

    # determine if current address is valid
    def is_valid_address(self, geo):
        try:
            self.location = geo.geocode(self.address, country_codes=['US'])
            self.latitude = self.location.latitude
            self.longitude = self.location.longitude
        except AttributeError:
            return False
        return True
