import requests


class TestAPI:

    def test_healthcheck(self):
        expected_status = 200
        expected_data = {}
        url = f'{"http://localhost:8080"}/healthcheck'
        response = requests.get(url)
        assert response.status_code == expected_status
        data = response.json()
        assert data == expected_data

    def test_invalid_hash(self):
        expected_error = {'validation_errors': 'post data must be json and contain string field'}
        url = f'{"http://localhost:8080"}/hash'
        response = requests.post(url)
        assert response.status_code == 400
        data = response.json()
        assert data == expected_error

    def test_empty_data_hash(self):
        expected_error = {'validation_errors': 'post data must be json and contain string field'}
        url = f'{"http://localhost:8080"}/hash'
        request_data = {}
        response = requests.post(url, data=request_data)
        assert response.status_code == 400
        data = response.json()
        assert data == expected_error

    def test_hash(self):
        url = f'{"http://localhost:8080"}/hash'
        request_data = {"string": "1231231"}
        response = requests.post(url, json=request_data)
        assert response.status_code == 200
        data = response.json()
        assert 'hash_string' in data
