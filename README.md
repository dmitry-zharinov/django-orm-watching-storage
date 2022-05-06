# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников банка. Он позволяет отображать информацию:
- об активных пропусках сотрудников, 
- об активных посещениях и их длитильности, 
- обо всех посещениях и их длительности по выбранному сотруднику.

В случае, если длительность посещения будет превышать 60 минут, в графе "Был ли визит подозрителен" отобразится статус `True`

### Запуск

1. Предварительно должен быть установлен Python3.
2. Для установки зависимостей:
```
pip install -r requirements.txt
```
3. Для запуска сайта:
```
$ python manage.py runserver 0.0.0.0:8000
```
4. Перейдите на сайт по адресу [http://localhost:8000](http://localhost:8000)

### Переменные окружения

Настройки для доступа К БД (хост, порт, имя, пользователь, пароль, секретный ключ) и настройки режиа отладки берутся из переменных окружения. Создайте файл `.env` и сохраните данные в него:

```
DATABASES_HOST=

DATABASES_PORT=

DATABASES_NAME=

DATABASES_USER=

DATABASES_PASSWORD=

SECRET_KEY=

DEBUG=False

```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).