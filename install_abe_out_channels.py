import channels
import warnings

username = 'root@openhim.org'
password = 'password'
apiUrl = 'https://10.147.72.11:8080'
rejectUnauthorized = False

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    channel_lists = channels.ta_channels + channels.cr_channels + channels.fr_channels + channels.hwr_channels + channels.shr_channels
    for channel_list in channel_lists:
        channels.install_passthrough_channel(username, password, apiUrl, rejectUnauthorized, channel_list)