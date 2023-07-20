from unittest import mock

from sample import random_sum, silly


@mock.patch("sample.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7


@mock.patch("sample.random.randint")
@mock.patch("sample.time.time")
@mock.patch("sample.requests")
def test_silly(mock_requests, mock_time, mock_randint):
    test_params = {
        "timestamp": 123456789,
        "number": 5,
    }
    mock_time.return_value = test_params["timestamp"]
    mock_randint.return_value = test_params["number"]

    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"args": test_params}
    mock_requests.get.return_value = mock_response
    assert silly() == test_params