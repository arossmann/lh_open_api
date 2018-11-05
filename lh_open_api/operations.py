import lh_open_api.request as request

base_url = 'https://api.lufthansa.com/v1/operations/'


def get_flight_schedules(origin, destination, from_date_time):
    """
    getting flight schedules
    :param origin:
    :param destination:
    :param from_date_time:
    :return schedule json object:
    """
    url = base_url+'schedules/'+origin+'/'+destination+'/'+from_date_time
    return request.make_request(url)


def get_flight_status(flight_number, date):
    """
    getting flight status.
    The available date range is from 7 days in the past until 5 days in the future.
    :param flight_number:
    :param date:
    :return flight status json object:
    """
    url = base_url+'flightstatus/'+flight_number+'/'+date
    return request.make_request(url)


def get_flight_route(origin, destination, date):
    """
    Retrieve the status of flights between two airports on a given date. The available date range is from yesterday
    until 5 days in the future. At most the first 80 matching flights will be returned.
    :param origin:
    :param destination:
    :param date:
    :return route json object:
    """
    url = base_url+'flightstatus/route/'+origin+'/'+destination+'/'+date
    return request.make_request(url)


def get_arrivals(airport_code, from_date_time):
    """
    Retrieve the status of all flights arriving at a specific airport within a given time range which is set to 4 hours
    by default starting from time value quoted within fromDateTime input parameter.
The permitted range for flights returned is from yesterday until 5 days in the future in 4 hours ranges. At most 80
flights will be returned.
    :param airport_code:
    :param from_date_time:
    :return arrivals json object:
    """
    url = base_url+'arrivals/'+airport_code+'/'+from_date_time
    return request.make_request(url)


def get_departures(airport_code, from_date_time):
    """
    Retrieve the status of all flights departing from a specific airport within a given time range. The permitted range
    is from yesterday until 5 days in the future. At most 80 flights will be returned.
    :param airport_code:
    :param from_date_time:
    :return departures json object:
    """
    url = base_url+'departures/'+airport_code+'/'+from_date_time
    return request.make_request(url)
