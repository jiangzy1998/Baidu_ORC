import requests


class web_request:

    def __init__(self, image_base64, access_token):
        self.image_base64 = image_base64
        self.access_token = access_token

    def json_request(self):
        language_type = 'CHN_ENG'
        detect_direction = 'true'
        detect_language = 'false'
        probability = 'true'
        image_host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + self.access_token
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        values = {
                'image': self.image_base64,
                'language_type': language_type,
                'detect_direction': detect_direction,
                'detect_language': detect_language,
                'probability': probability
                }
        req = requests.post(image_host, data=values, headers=head)
        json_req = req.json()
        return json_req
