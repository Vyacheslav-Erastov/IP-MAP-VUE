#Приступим к работе

---

### Запуск API

---

Для начало нужно перейти в директорию с проектом на Django REST. 
Для этого в командной строке пишем:
```
$ cd <путь к директории с проектом>/DemoRest
```

Предварительно нужно скачать компоненты необходимые для запуска
проекта, введя следующие команды:

```

$ pip install django

$ pip install djangorestframework

$ pip install corsheaders

```
Далее в [DemoRest/settings.py](./DemoRest/settings.py) на месте
DATABASES вводим данные своей БД. 

Пример с PostgreSQL:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Если вы используете PostgreSQL, то дополнительно нужно ввести
следующую команду (для Windows):

```

.\DemoRest> pip install psycopg2

```

Для Linux:

```

$ pip install psycopg2 binary

```
Далее для связи с БД и инициализации проекта вводим следующие
команды:
```
$ manage.py makemigrations
$ manage.py migrate
```
Далее для запуска локального сервера вводим команду:
```
$ manage.py runserver
```
Если вы сделали все правильно в командной строке должно 
появиться сообщение:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 03, 2022 - 22:02:36
Django version 4.0.5, using settings 'DemoRest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Далее можно перейти по ссылке на локальный сервер 
`http://127.0.0.1:8000/api/v1/ipinfo/ip/` и 
протестировать само API, так как у Django REST 
есть удобный web-интерфейс для этого.

Далее, для запуска web-приложения нужно запустить проект на Vue.

### Запуск web-приложения на Vue

---

Для запуска web-приложения нужно, также перейти в директорию
с проектом на Vue.
Для этого в командной строке пишем:
```
$ cd <путь к директории с проектом>/vue-ip-info
```

Предварительно нужно скачать компоненты необходимые 

для запуска проекта, введя следующие команды:

```

$ npm install vue

$ npm install axios

```
Далее для запуска локального сервера, на котором будет работать
наше web-приложение нужно ввести команду:
```
$ npm run serve
```
Если вы сделали все правильно в командной 
строке должно появиться сообщение:
```
  App running at:
  - Local:   http://localhost:8081/
  - Network: http://192.168.x.x:8081/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```
Далее можно перейти по ссылке на локальный 
сервер `http://localhost:8081/` и web-приложение 
запущено!


Таким образом должно выглядеть запущенное web-приложение:


![IP INFO start](./IP%20INFO%20start.jpg)

Таким образом после ввода _2.2.2.2_:


![IP INFO work](./IP%20INFO%20work.jpg)
