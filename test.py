from src.Translator import Translator
from src.FilmFinder import FilmFinder
from src.RequestManager import RequestManager


def test_translate_into_english():
    translator = Translator()
    translated_words_into_english = ["Шрек", "Привет", "Машина"]
    answer = ["Shrek", "Hello", "Machine"]

    for index, word in enumerate(translated_words_into_english):
        assert translator.translate_into_english(word) == answer[index]


def test_translate_into_russian():
    translator = Translator()
    translated_words_into_english = ["Shrek", "Hello", "Machine"]
    answer = ["Шрек", "Привет", "Машина"]

    for index, word in enumerate(translated_words_into_english):
        assert translator.translate_into_russian(word) == answer[index]


def test_find_film():
    translator = Translator()
    request_manager = RequestManager()
    film_finder = FilmFinder(request_manager, translator)
    answer = "<b>Название фильма</b>: <em>Шрек</em> (Shrek)"

    assert film_finder.get_film_characteristics("Шрек").split("\n")[0] == answer
