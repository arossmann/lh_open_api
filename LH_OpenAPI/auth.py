import requests
import configparser

def get_auth_token():
    """
    get the authentication token
    :return: auth token
    """
    # read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    # set variables
    secret = config['LH_OPENAPI']['LH_SECRET']
    key = config['LH_OPENAPI']['LH_KEY']
    token_url = config['LH_OPENAPI']['LH_TOKEN_URL']
    data = {'client_id': key, 'client_secret': secret, 'grant_type': 'client_credentials'}

    r = requests.post(token_url, data=data)
    if r.status_code == 200:
        token_string = r.json()
        return token_string['access_token']
    else:
        return 'invalid token'


def get_header():
    """
    getting the header with authorization token
    :return: header for further requests
    """
    token = get_auth_token()
    headers = {'Accept': 'application/json', 'Authorization':'Bearer '+token}
    return headers
