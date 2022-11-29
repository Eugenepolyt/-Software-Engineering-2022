from RequestManager import RequestManager
import translators as tss


class RandomFilm:

    def __init__(self, request_manager, translator):
        self.request_manager = request_manager
        self.translator = translator

    def get_random_film_description(self):

        response = self.request_manager.get_random_film()
        name = str(response['name'])
        age = str(response['releaseYear'])
        genre = str(response['genre'])
        runtime = str(response['runtime'])
        imdb_rating = str(response['imdbRating'])
        overview = str(response['overview'])

        parts_of_messages = [name, age, genre, runtime, imdb_rating, overview]

        return self.translator.get_html_ru_categories(parts_of_messages)




