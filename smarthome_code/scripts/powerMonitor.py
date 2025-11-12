import requests


class PowerMonitor:

    # thermometer constructor
    def __init__(self, EntityID, homeAssistantUrl, accessToken):
        self.EntityID = EntityID  # which thermometer to connect to
        self.homeAssistantUrl = homeAssistantUrl  # where the home assitant live
        self.accessToken = accessToken  # proving Identity

    # Sends a request given a entityID.
    def sendRequest(self):
        # send request to this location
        URL = self.homeAssistantUrl + "/api/states/" + self.EntityID
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
            print("Failed to get response from Outlet")
            return None

    # Returns temp in fahrenheit and converts it celcius.
    def watts(self):
        watts = self.sendRequest()
        if watts is not None:
            print(f"Watts: {watts:.1f}")
        return watts
