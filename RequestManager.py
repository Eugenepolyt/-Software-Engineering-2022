import requests


class RequestManager:
    API_KEY = "fe0f184"

    def get_film_with_name(self, name):
        parametres = {'t': name, "apikey": self.API_KEY}
        respone = requests.get("http://www.omdbapi.com/", params=parametres)
        return respone.json()

