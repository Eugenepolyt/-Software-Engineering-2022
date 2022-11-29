from RequestManager import RequestManager
import translators as tss


class RandomFilm:

    def __init__(self, request_manager, translator):
        self.request_manager = request_manager
        self.translator = translator

    def get_random_film_description(self):

        response = self.request_manager.get_random_film()
        if not response[1]:
            return "Извините, но сервер недоступен, попробуйте позже"
        name = str(response[0]['name'])
        age = str(response[0]['releaseYear'])
        genre = str(response[0]['genre'])
        runtime = str(response[0]['runtime'])
        imdb_rating = str(response[0]['imdbRating'])
        overview = str(response[0]['overview'])

        parts_of_messages = [name, age, genre, runtime, imdb_rating, overview]

        return self.translator.get_html_ru_categories(parts_of_messages)




