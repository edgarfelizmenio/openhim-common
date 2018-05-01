import requests
import utils

def install_passthrough_channel(username, password, apiUrl, rejectUnauthorized, channel):    
    uri = '{}/channels'.format(apiUrl)
    utils.authenticate(username, apiUrl, rejectUnauthorized)
    headers = utils.generate_auth_headers(username, password)
    response = requests.post(uri, headers=headers, json=channel, verify=rejectUnauthorized)
    
    if (response.status_code == 201):
        print("Channel successfully installed.")
    else:
        print('Received a non-201 response code, the response body was:{}'.format(response.text))

def get_all_channels(username, password, apiUrl, rejectUnauthorized):
    uri = '{}/channels'.format(apiUrl)
    utils.authenticate(username, apiUrl, rejectUnauthorized)
    headers = utils.generate_auth_headers(username, password)
    response = requests.get(uri, headers=headers, verify=rejectUnauthorized)
    if (response.status_code == 200):
        print("Retrieved all channels.")
        return response.json()
    else:
        print('Received a non-201 response code, the response body was:{}'.format(response.text))
    return {}

def delete_channel(username, password, apiUrl, rejectUnauthorized, channelId):
    uri = '{}/channels/{}'.format(apiUrl, channelId)
    utils.authenticate(username, apiUrl, rejectUnauthorized)
    headers = utils.generate_auth_headers(username, password)
    response = requests.delete(uri, headers=headers, verify=rejectUnauthorized)
    if (response.status_code == 200):
        print("Deleted channel {}.".format(channelId))
    else:
        print('Received a non-201 response code, the response body was:{}'.format(response.text))

default_routes = {
    'TA': {
        'name': 'Trusted Authority',
        'host': '10.147.72.14',
        'port': 80,
        'type':'http',
        'secured': False,
        'primary': True,
    },
    'CR': {
        'name': 'Client Registry',
        'host': '10.147.72.15',
        'port': 80,
        'type': 'http',
        'secured': False,
        'primary': True
    },
    'FR': {
        'name': 'Facilities Registry',
        'host': '10.147.72.16',
        'port': 80,
        'type': 'http',
        'secured': False,
        'primary': True,
    },
    'HWR': {
        'name': 'Healthcare Worker Registry',
        'host': '10.147.72.17',
        'port': 80,
        'type': 'http',
        'secured': False,
        'primary': True
    },
    'SHR': {
        'name': 'Shared Health Record',
        'host': '10.147.72.13',
        'port': 80,
        'type':'http',
        'secured': False,
        'primary': True, 
    }
}

ta_channels = [{
    'name': 'Get Master Key',
    'urlPattern': '^/masterkey$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['TA']]
},{
    'name': 'Get or Update User',
    'urlPattern': '^/user/.*(?<!/sk)$',
    'allow': ['tut'],
    'methods': ['GET', 'PUT'],
    'routes': [default_routes['TA']]
},{
    'name': 'Add User',
    'urlPattern': '^/user$',
    'allow': ['tut'],
    'methods': ['POST'],
    'routes': [default_routes['TA']]
},{
    'name': 'Get One Time Key of User',
    'urlPattern': '^/user/.*(?<=/sk)$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['TA']]
}]

cr_channels = [{
    'name': 'Get Person IDs',
    'urlPattern': '^/person$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['CR']]
},{
    'name': 'Get Person',
    'urlPattern': '^/person/.*$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['CR']]
},{
    'name': 'Add Patient or Get All Patients',
    'urlPattern': '^/patient$',
    'allow': ['tut'],
    'methods': ['GET', 'POST'],
    'routes': [default_routes['CR']]
},{
    'name': 'Add, Get, or Delete Patient',
    'urlPattern': '^/patient/.*$',
    'allow': ['tut'],
    'methods': ['GET', 'PUT', 'DELETE'],
    'routes': [default_routes['CR']]
}]

fr_channels = [{
    'name': 'Get Location by ID',
    'urlPattern': '^/location/.*$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['FR']]
},{
    'name': 'Get all locations',
    'urlPattern': '^/location$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['FR']]
}]

hwr_channels = [{
    'name': 'Get Provider by ID',
    'urlPattern': '^/provider/.*$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['HWR']]
},{
    'name': 'Get all provider IDs',
    'urlPattern': '^/provider$',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['HWR']]
}]

shr_channels = [{
    'name': 'Get or Add Encounters based on patient ID',
    'urlPattern': '^/encounters/patient/.*$',
    'allow': ['tut'],
    'methods': ['GET', 'POST'],
    'routes': [default_routes['SHR']]
},{
    'name': 'Return an Encounter based on encounter ID',
    'urlPattern': '^/encounters/.*',
    'allow': ['tut'],
    'methods': ['GET'],
    'routes': [default_routes['SHR']]
},{
    'name': 'Add an Encounter or Get all Encounter ids',
    'urlPattern': '^/encounters$',
    'allow': ['tut'],
    'methods': ['GET', 'POST'],
    'routes': [default_routes['SHR']]
}]

