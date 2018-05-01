import warnings
import channels

username = 'root@openhim.org'
password = 'password'
apiUrl = 'https://10.147.72.11:8080'
rejectUnauthorized = False

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    channels_list = channels.get_all_channels(username, password, apiUrl, rejectUnauthorized)
    for channel in channels_list:
        channels.delete_channel(username, password, apiUrl, rejectUnauthorized, channel['_id'])