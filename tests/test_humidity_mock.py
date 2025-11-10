from smarthome_code.scripts.humidity import humidity
# lets us create a fake object or humidity function
from unittest.mock import patch, MagicMock
# so we can test without connecting to api
import pytest


def test_sendRequest():
    # thermometer test object
    h = humidity("sensor.fake_humidity", "http://fake-url", "fake_token")

    with patch("smarthome_code.scripts.humidity.requests.get") as mock_get:
        mock_response = MagicMock()  # make a fake method
        mock_response.status_code = 200  # first thing request.get is expecting
        # second thing request.get is expecting
        mock_response.json.return_value = {"state": 61.3}
        mock_get.return_value = mock_response  # mock_get returns this fake value

        result = h.sendRequest()  # send a request

        assert result == 61.3  # check that results match expectation
