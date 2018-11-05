import requests
import LH_OpenAPI.auth as auth
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='LHOpenAPI.log',
    filemode='a',
    format='%(asctime)s -%(levelname)s- %(message)s')


def make_request(url):
    """
    makes the request to the URL
    :param url:
    :return json object:
    """
    header = auth.get_header()
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        logging.info('request to URL ' + url + ' status: ' + str(r.status_code))
        return r.text
    else:
        logging.info('request to URL ' + url + ' status: ' + str(r.status_code) + ' message: '+r.text)
        return 'invalid request'
