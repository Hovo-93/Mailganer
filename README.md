## Небольшой сервис для отправки имейл рассылок 

## Описание

Список технологий: Python, Django, Docker, db.sqlite3, Celery, Redis

#### Задача:

1.Отправка рассылок с использиванием html макета и списка подписчиков

2.Отправка отложенных рассылок

3.Использивание переменных в макете рассылки.(Пример:имя,фамилия,день рождения
из списка подписчиков)

4.Отслеживание открытий писем реализовать при помощи Celery


## Подготовка и запуск проекта
#### Шаг 1. Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
```bash
docker -v
```
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 2. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/Mailganer.git
```


#### Шаг 3. Создайте в клонированной директории файл .env
Пример:
```bash

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email'
EMAIL_HOST_PASSWORD = 'your_email_password'

```
#### Шаг 4.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```
#####Создаем  суперюзера для входа в Django Admin

#### Шаг 5. Выполняем комманду
```python
    pip install -r requirements.txt
```
#### Шаг 6. Запуск Redis через Docker
```
 Для Windows в CMD:
    1.pull redis  
    2.docker run -d -p 6379:6379 --name redis
 
```
### После успешной установки запускаем сервер 
```python
python manage.py runserver
```

#### Переходим в админку
1. Создаем подписчиков(subscribers)
2. 

#### Запуск Celery

```
Для Windows:
    celery -A mailganer worker -l info --pool=solo
    celery -A mailganer beat -l info 
```
