import os
import json
import configparser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
config = configparser.ConfigParser()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    config.read("config.ini")
except FileNotFoundError:
    print("Can't find config file config.ini, please set up")
    exit(-1)

onDesktop = config['Machine'].getboolean('onDesktop')

SpotifyIDs = config['Spotify']
DesktopIds = config['ControlMyMonitorDesktop']
LaptopIds = config['ControlMyMonitorLaptop']

# Secret Secret, don't commit to git (generated at developer.spotify.com)

#
# headers = {
#     "Accept": "application/json",
#     "Content-type": "application/json",
#     "Authorization": "Bearer " + oAuth
# }

data = {
    "device_ids": [SpotifyIDs['Laptop'] if onDesktop else SpotifyIDs['Desktop']]
}

auth_data = {
    "client_id": "39b288554cf348daac20be0ee0c0e305",
    "response_type": "token",
    "redirect_uri": "https://google.com"
    # "scope": "app-remote-control"
}

# Not ideal but the monitorcontrol library is inconsistent, ControlMyMonitor uses absolute IDs
# subprocess.run(["switch.bat"], capture_output=True)

cid ="39b288554cf348daac20be0ee0c0e305"
secret = open("secret", "r").read()
uri = "https://google.com"
testusername = "1233011061"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="app-remote-control user-read-playback-state user-modify-playback-state", client_id=cid, client_secret=secret, redirect_uri=uri, username=testusername))
# print(sp.current_playback())
sp.transfer_playback(device_id=SpotifyIDs['Desktop'])

