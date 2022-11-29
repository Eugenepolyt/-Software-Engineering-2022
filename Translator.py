import translators as tss


class Translator:

    def get_html_ru_categories(self, parts_of_messages):
        parts_of_messages_str = ''
        for i in parts_of_messages:
            parts_of_messages_str += i + '\n'

        translated_part_of_messages = self.translate_into_russian(parts_of_messages_str)
        categories = ['Название фильма',
                      'Дата выхода',
                      'Жанр',
                      'Продолжительность',
                      'Рейтинг IMDb',
                      'Описание фильма']

        return self.get_html_result(categories, translated_part_of_messages.split("\n"), parts_of_messages[0])

    def get_html_result(self, categories, data, name):
        result = ''
        for i, category in enumerate(categories):
            part_of_message = f'<b>{category}</b>: <em>{data[i]}</em>'
            if category == "Название фильма":
                result += part_of_message + f' ({name})\n'
            else:
                result += part_of_message + '\n'
        return result

    def translate_into_russian(self, data):
        return tss.bing(data, to_language="ru")

    def translate_into_english(self, data):
        return tss.bing(data, to_language="en")
