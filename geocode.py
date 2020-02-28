import requests
import json


class Addr2Geocode:

    def __init__(self, output_format="json", key_path="./key/api.key"):
        self.REQUEST_FORMAT = "https://maps.googleapis.com/maps/api/geocode/{}?address={}&key={}"
        self.output_format = output_format
        self.key_path = key_path

        def get_key():
            with open(self.key_path, 'r') as f:
                key = f.read()
            return key

        self.key = get_key()

    def translate(self, addr):
        def clean_addr(addr):
            cleaned_addr = addr.replace(" ", "+")
            return cleaned_addr

        lat, long = None, None
        response = requests.get(self.REQUEST_FORMAT.format(self.output_format, clean_addr(addr), self.key))
        if response.status_code == 200:
            json_content = json.loads(response.content)
            if len(json_content['results']) > 0:
                first_response = json_content['results'][0]
                location = first_response['geometry']['location']
                lat, long = location['lat'], location['lng']
        return lat, long


if __name__ == "__main__":
    test_addr = "西摩道11號福澤花園A座"
    geocode = Addr2Geocode()

    lat, long = geocode.translate(test_addr)

    print(lat, long)

