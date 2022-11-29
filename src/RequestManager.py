import requests


class RequestManager:
    API_KEY = "fe0f184"

    def get_random_film(self):
        response = requests.get("https://k2maan-moviehut.herokuapp.com/api/random")
        if response.status_code >= 200 or response.status_code <= 299:
            return {}, False

        return response.json(), True

    def get_film_with_name(self, name):
        parametres = {'t': name, "apikey": self.API_KEY}
        respone = requests.get("http://www.omdbapi.com/", params=parametres)
        return respone.json()

