import channels
import warnings

username = 'root@openhim.org'
password = 'password'
apiUrl = 'https://10.147.72.11:8080'
rejectUnauthorized = False

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    channel_list = channels.ta_channels
    for channel in channel_list:
        channels.install_passthrough_channel(username, password, apiUrl, rejectUnauthorized, channel)