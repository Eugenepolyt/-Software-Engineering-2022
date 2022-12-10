# Телеграм бот для получения фильмов

### Описание

------------
Данный бот поможет вам получить статистику нужного вам фильма с imdb и поможет подобрать фильм на ночь :) 

### Тестирование
Merge в develop: 

[![Test-For-Imdb-Bot](https://github.com/Eugenepolyt/-Software-Engineering-2022/actions/workflows/testing.yml/badge.svg?branch=develop&event=push)](https://github.com/Eugenepolyt/-Software-Engineering-2022/actions/runs/3665166044)

Merge в master: 

[![Test-For-Imdb-Bot](https://github.com/Eugenepolyt/-Software-Engineering-2022/actions/workflows/testing.yml/badge.svg?branch=master&event=push)](https://github.com/Eugenepolyt/-Software-Engineering-2022/actions/runs/3665281999)


### Как запустить? ( Docker )

------------

Для того чтобы запустить бот при помощи докера необязательно копировать проект, чтобы воспользоваться ботом нужно:
- Установить докер
- Ввести следующие команды в терминал:

`docker pull jykaswift/imdb_bot`

`docker run jykaswift/imdb_bot`

### Как запустить?

------------


Для того чтобы запустить бота без докера:
1. Склонируйте репозиторий себе на комьютер:
`git clone https://github.com/Eugenepolyt/-Software-Engineering-2022.git`
2. Установите python версии 3.10
3. Перейдите в папку с проектом и установите нужные библиотеки при помощи команды в терминале:
`pip install -r requirements.txt`
4. Запустите python main файл командой:
`python main.py`

### Как работать с ботом?

Как искать фильм? Для этого в боте есть специальная кнопка, нажимаете ее , вводите название фильма и получаете результат, для получения случайного фильма есть другая кнопка, которую достаточно просто нажать.

[![](https://yapcdn.net/se4/33/zOCbzni.png)](https://yapcdn.net/se4/33/zOCbzni.png)

[![](https://yapcdn.net/se4/33/7IuMjRWM.png)](https://yapcdn.net/se4/33/7IuMjRWM.png)



