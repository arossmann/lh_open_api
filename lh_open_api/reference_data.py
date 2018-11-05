import LH_OpenAPI.request as request

base_url = 'https://api.lufthansa.com/v1/references/'


def get_airport_data(iata_airport):
    """
    getting details for airport
    :param iata_airport:
    :return airport json object:
    """
    url = base_url+'airports/'+iata_airport
    return request.make_request(url)


def get_aircraft_data(aircraft_code='ALL'):
    """
    A directory of all available aircraft. You can retrieve the full set or details of one particular aircraft.
    :param aircraft_code:
    :return aircraft json object:
    """
    if aircraft_code == 'ALL':
        url = base_url + 'aircraft/'
    else:
        url = base_url+'aircraft/'+aircraft_code
    return request.make_request(url)


def get_airline_data(iata_airline):
    """
    getting details for airline
    :param iata_airline:
    :return airline json object:
    """
    url = base_url+'airlines/'+iata_airline
    return request.make_request(url)


def get_countries_data(country_code):
    """
    getting details for country
    :param country_code:
    :return country json object:
    """
    url = base_url+'countries/' + country_code
    return request.make_request(url)


def get_cities_data(city_code):
    """
    getting details for city
    :param city_code:
    :return city json object:
    """
    url = base_url+'cities/' + city_code
    return request.make_request(url)


def get_nearest_airports(lat, long):
    """
    get nearest airports for latitude and longitude
    :param lat:
    :param long:
    :return airports json object:
    """
    url = base_url+'airports/nearest/'+str(lat)+','+str(long)
    return request.make_request(url)
