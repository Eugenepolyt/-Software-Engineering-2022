class FilmFinder:

    def __init__(self, request_manager, translator):
        self.request_manager = request_manager
        self.translator = translator

    def get_film_characteristics(self, name):
        translated_name = self.translator.translate_into_english(name)
        json_description = self.request_manager.get_film_with_name(translated_name)
        name = str(json_description['Title'])
        age = str(json_description['Year'])
        genre = str(json_description['Genre'])
        runtime = str(json_description['Runtime'])
        imdb_rating = str(json_description['imdbRating'])
        overview = str(json_description['Plot'])

        parts_of_messages = [name, age, genre, runtime, imdb_rating, overview]

        return self.translator.get_html_ru_categories(parts_of_messages)


