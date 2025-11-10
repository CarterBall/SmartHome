import requests


class soilMoistureSensor:

    # soilMoistureSensor constructor
    # SMS = soilMoistureSensor
    def __init__(self, SMS_EntityID, homeAssistantUrl, accessToken):
        self.SMS_EntityID = SMS_EntityID  # which Humidity reader to connect to
        self.homeAssistantUrl = homeAssistantUrl  # where the home assitant live
        self.accessToken = accessToken  # proving Identity

    # Sends a request given a entityID.
    def sendRequest(self):
        # send request to this location
        URL = self.homeAssistantUrl + "/api/states/" + self.humidityEntityID
        # authorization step
        headers = {
            "Authorization": "Bearer " + self.accessToken,
            "Content-Type": "application/json"
        }
        response = requests.get(URL, headers=headers)
        if (response.status_code == 200):
            data = response.json()
            return float(data["state"])
        else:
            print("Failed to get response from soil moisture sensor")
            return None

    # Returns the Moisture
    def moisture(self):
        moisture = self.sendRequest()
        if moisture is not None:
            print(f"Moisture: {moisture}%")
        return moisture
