import requests


class ResponseTests(object):

    # Given a training page request and the response should be successful
    def test_get_successful_response(self):
        resp = requests.get('https://techstepacademy.com/training-ground')
        assert resp.status_code == 200
