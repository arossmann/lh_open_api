import LH_OpenAPI as LH
import json


def get_flights(flight_query):
    """
    get flight codes for flight schedule as single array (without overhead from API)
    :param flight_query:
    :return array with flight codes:
    """
    flights = json.loads(LH.get_flight_schedules(flight_query['origin'],
                                                 flight_query['destination'],
                                                 flight_query['date']))
    flight_codes = []
    for value in flights['ScheduleResource']['Schedule']:
        if isinstance(value['Flight'], list):
            connecting_flight = []
            for data in value['Flight']:
                connecting_flight.append(
                    data['MarketingCarrier']['AirlineID'] +
                    str(data['MarketingCarrier']['FlightNumber']))
            flight_codes.append(connecting_flight)
        if isinstance(value['Flight'], dict):
            flight_codes.append(
                value['Flight']['MarketingCarrier']['AirlineID'] +
                str(value['Flight']['MarketingCarrier']['FlightNumber']))
    return flight_codes


def publish_flight_information(flight_codes, flight_query):
    """
    publish the flight status information
    :param flight_codes:
    :param flight_query:
    """
    for flight_code in flight_codes:
        if isinstance(flight_code, list):
            print('connecting flight ')
            for single_flight in flight_code:
                print(LH.get_flight_status(single_flight, flight_query['date']))
        if isinstance(flight_code, str):
            print('single flight')
            print(LH.get_flight_status(flight_code, flight_query['date']))


if __name__ == "__main__":
    query_FRA_JFK = {
        'origin': 'FRA',
        'destination': 'JFK',
        'date': '2018-09-24'}
    publish_flight_information(get_flights(query_FRA_JFK), query_FRA_JFK)

