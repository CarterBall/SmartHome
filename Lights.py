import requests
# "hs_color": [120, 100] → hue & saturation
# "xy_color": [0.323, 0.329] → CIE coordinates
# "brightness": 255 → full brightness
# "brightness_pct": 50 → 50% brightness


class Lights:

    def __init__(self, entityID, homeAssistantUrl, accessToken):
        self.entityID = entityID  # which light to connect to
        self.homeAssistantUrl = homeAssistantUrl  # where the home assitant live
        self.accessToken = accessToken  # proving Identity
        self.brightnessPercent = 60  # min 0 max 100

    def sendReguest(self, request):
        # send request to this location
        URL = self.homeAssistantUrl + "/api/services/light/" + request
        # authorization step
        headers = {
            "Authorization": "Bearer " + self.accessToken,
            "Content-Type": "application/json"
        }
        # what light bulb and  request
        if (request == "turn_on"):
            data = {"entity_id": self.entityID,
                    "brightness_pct": self.brightnessPercent}
        elif (request == "turn_off"):
            data = {"entity_id": self.entityID}
        # send the request
        response = requests.post(URL, headers=headers, json=data)
        # home assitant responding message
        print(response.text)
        print(response.status_code)

    def On(self):
        self.sendReguest("turn_on")

    def Off(self):
        self.sendReguest("turn_off")
