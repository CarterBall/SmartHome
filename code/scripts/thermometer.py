import requests


class thermometer:

    # thermometer constructor
    def __init__(self, tempEntityID, homeAssistantUrl, accessToken):
        self.tempEntityID = tempEntityID  # which thermometer to connect to
        self.homeAssistantUrl = homeAssistantUrl  # where the home assitant live
        self.accessToken = accessToken  # proving Identity

    # Sends a request given a entityID.
    def sendRequest(self):
        # send request to this location
        URL = self.homeAssistantUrl + "/api/states/" + self.tempEntityID
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

    # Returns temp in fahrenheit and converts it celcius.
    def celsius(self):
        temp = self.sendRequest()
        if temp is not None:
            c = (temp - 32) * 5 / 9
            print(f"Temperature: {c:.1f}°C")
        return temp

    # Returns fahrenheit by default
    def fahrenheit(self):
        temp = self.sendRequest()
        if temp is not None:
            print(f"Temperature: {temp}°F")
        return temp
