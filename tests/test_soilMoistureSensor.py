from smarthome_code.scripts.soilMoistureSensor import soilMoistureSensor
# lets us create a fake object or moisture function
from unittest.mock import patch, MagicMock
# so we can test without connecting to api
import pytest


def test_sendRequest():
    # thermometer test object
    s = soilMoistureSensor("sensor.fake_MoistureSensor",
                           "http://fake-url", "fake_token")

    with patch("smarthome_code.scripts.soilMoistureSensor.requests.get") as mock_get:
        mock_response = MagicMock()  # make a fake method
        mock_response.status_code = 200  # first thing request.get is expecting
        # second thing request.get is expecting
        mock_response.json.return_value = {"state": 61.3}
        mock_get.return_value = mock_response  # mock_get returns this fake value

        result = s.sendRequest()  # send a request

        assert result == 61.3  # check that results match expectation
