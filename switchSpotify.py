import requests
import json

DESKTOP = "5a481e245c3563e798f28f305211f02c0518edd2"
LAPTOP = "3a189740fe35cb5e4c21ae694a82619b5957d629"

onDesktop = False

oAuth = open("secret", "r").read()

headers = {
    "Accept": "application/json",
    "Content-type": "application/json",
    "Authorization": "Bearer " + oAuth
}

# parameters = {
#     "device_ids": [LAPTOP if onDesktop else DESKTOP]
# }

data = {
  "device_ids": [LAPTOP if onDesktop else DESKTOP]
}
# getDevices = requests.get("https://api.spotify.com/v1/me/player/devices", headers=headers)
switchDevices = requests.put("https://api.spotify.com/v1/me/player", data=json.dumps(data), headers=headers)
# print(getDevices.text)
print(switchDevices.text)
