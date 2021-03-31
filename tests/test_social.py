import requests


class SocialLinksTextTests(object):

    # Given a training page request and the response should be contains twitter link text
    def test_twitter_is_present(self):
        resp = requests.get('https://techstepacademy.com/training-ground')
        assert "twitter" in resp.text
