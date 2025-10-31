import requests


class thermometer:

    def __init__(self, entityID, homeAssistantUrl, accessToken):
        self.entityID = entityID  # which light to connect to
        self.homeAssistantUrl = homeAssistantUrl  # where the home assitant live
        self.accessToken = accessToken  # proving Identity

    def sendRequest(self):
        # send request to this location
        URL = self.homeAssistantUrl + "/api/states/" + self.entityID
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

    def celsius(self):
        temp = self.sendRequest()
        if temp is not None:
            print(f"Temperature: {temp}°C")
        return temp

    def fahrenheit(self):
        temp = self.sendRequest()
        if temp is not None:
            print(f"Temperature: {temp * 9/5 + 32}°F")
        return temp
