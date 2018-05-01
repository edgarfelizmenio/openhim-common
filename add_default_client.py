import requests
import utils
import warnings

username = 'root@openhim.org'
password = 'password'
apiURL = 'https://10.147.72.11:8080'
rejectUnauthorized = False

def create_default_client(client_id, name, client_doman, roles, password):
    default_client = {
        'clientID': client_id,
        'name': name,
        'clientDomain': client_doman,
        'roles': roles
    }
    password_object = utils.create_password_object(password)
    default_client['passwordAlgorithm'] = password_object['userPasswordAlgorithm']
    default_client['passwordHash'] = password_object['userPasswordHash']
    default_client['passwordSalt'] = password_object['userPasswordSalt']
    return default_client

def save_default_client(apiURL, username, salt, timestamp, token, default_client):
    response = requests.post('{}/clients'.format(apiURL),
                            verify=False,
                            json=default_client,
                            headers={
                                'auth-username': username,
                                'auth-ts': timestamp,
                                'auth-salt': salt,
                                'auth-token': token
                            })
    print(response.status_code)
    if response.status_code == 201:
        print('Default user saved.')
    else:
        raise Exception('Failed to save default user!!!\n{}'.format(response.content))

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    utils.authenticate(username,apiURL,rejectUnauthorized)
    auth_headers = utils.generate_auth_headers(username, password)
    timestamp = auth_headers['auth-ts']
    salt = auth_headers['auth-salt']
    token = auth_headers['auth-token']

    default_client = create_default_client('tutorial',
                                        'OpenHIM Tutorial Client',
                                        '10.147.72.11',
                                        ['tut'],
                                        'pass')
    save_default_client(apiURL,
                        username,
                        salt,
                        timestamp,
                        token,
                        default_client)
