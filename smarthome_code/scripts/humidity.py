import requests


class humidity:

    # thermometer constructor
    def __init__(self, humidityEntityID, homeAssistantUrl, accessToken):
        self.humidityEntityID = humidityEntityID  # which Humidity reader to connect to
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
            print("Failed to get response from lights")
            return None

    # Returns the humidity
    def humidity(self):
        humidity = self.sendRequest()
        if humidity is not None:
            print(f"Humidity: {humidity}%")
        return humidity
