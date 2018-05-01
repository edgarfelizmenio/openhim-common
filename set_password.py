# authenticateUser
# createAuthHeaders
# changePassword
# updateUserPasswordToken

import utils
import requests
import warnings

def changePassword(username, timestamp, salt, token, new_password_object, rejectUnauthorized):
    print('New password created.')
    print('Changing password...')

    response = requests.put('{}/users/{}'.format(apiURL, username),
                verify=rejectUnauthorized,
                json = {
                    'passwordAlgorithm': new_password_object['userPasswordAlgorithm'],
                    'passwordSalt': pass_salt,
                    'passwordHash': pass_hash,
                },
                headers = {
                    'auth-username': username,
                    'auth-ts': timestamp,
                    'auth-salt': salt,
                    'auth-token': token
                })
                
    print(response.status_code)
    if response.status_code == 200:
        print("Updated password.")
    else:
        print("Nah bitch")
        raise Exception('password not updated! {}'.format(response.status_code))

def updateUserPasswordToken(username, timestamp, salt, token, new_token, rejectUnauthorized):
    print("Updating user password token... {}".format(token))
    response = requests.put('{}/token/{}'.format(apiURL,token),
                verify = rejectUnauthorized,
                headers = {
                    'auth-username': username,
                    'auth-ts': timestamp,
                    'auth-salt': salt,
                    'auth-token': new_token
                })
    print(response.status_code)
    if response.status_code == 200:
        # print(response.json)
        print("Updated password token")
    else:
        print("Nah bitch")
        print(response.content)
        raise Exception('Password token not updated! {}'.format(response.status_code))

apiURL = 'https://10.147.72.11:8080'
username = 'root@openhim.org'
old_password = 'openhim-password'
new_password = 'password'
rejectUnauthorized = False

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    utils.authenticate(username, apiURL, rejectUnauthorized)
    auth_headers = utils.generate_auth_headers(username, old_password)

    username = auth_headers['auth-username']
    timestamp = auth_headers['auth-ts']
    salt = auth_headers['auth-salt']
    token = auth_headers['auth-token']
    # print(timestamp)

    password_object = utils.create_password_object(new_password)
    pass_salt = password_object['userPasswordSalt']
    pass_hash = password_object['userPasswordHash']

    changePassword(username, timestamp, salt, token, password_object, rejectUnauthorized)

# shasum = hashlib.sha512()
# shasum.update((pass_hash + pass_salt + timestamp).encode('utf-8'))
# new_token = shasum.hexdigest()
# updateUserPasswordToken(username, timestamp, salt, token, new_token, rejectUnauthorized)

# auth_headers = utils.generate_auth_headers(username, new_password)

# print(auth_headers['auth-username'])
# print(auth_headers['auth-ts'])
# print(auth_headers['auth-salt'])
# print(auth_headers['auth-token'])

# new_token = auth_headers['auth-token']
# print('old token: {}'.format(token))
# print('new token: {}'.format(new_token))
# updateUserPasswordToken(username, timestamp, salt, token, new_token, rejectUnauthorized)

