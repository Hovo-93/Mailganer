## Небольшой сервис для отправки имейл рассылок 

## Описание

Список технологий: Python, Django, Docker, db.sqlite3, Celery, Redis

#### Задача:

1.Отправка рассылок с использованием html макета и списка подписчиков

2.Отправка отложенных рассылок

3.Использование переменных в макете рассылки.(Пример:имя,фамилия,день рождения
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
#### Если Вы хотите отправить рассылку со своей почты, то необходимо:
1. Войти в [myaccount](https://myaccount.google.com/security?hl=ru)
2. Сгенерировать пароль для приложения
3. Зарегистрировать его в .env как
```python
EMAIL_HOST_PASSWORD = 'new_password'
```
#### Шаг 4.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```
#### Шаг 5.Создаем  суперюзера для входа в Django Admin
```python
    python manage.py createsuperuser
```
#### Шаг 6. Выполняем комманду
```python
    pip install -r requirements.txt
```
#### Шаг 7. Запуск Redis через Docker
```
 Для Windows в CMD:
    1.pull redis  
    2.docker run -d -p 6379:6379 --name redis
 
```
#### Шаг 8. После успешной установки запускаем сервер 
```python
python manage.py runserver
```

#### Шаг 9. Переходим в админку
1. Создаем подписчиков [Subscribers](http://127.0.0.1:8000/admin/sending_emails/subscriber/)
2. Создаем рассылку [Newsletter](http://127.0.0.1:8000/admin/sending_emails/newsletter/)
3. При вводе названия шаблона, необходимо добавить .html
```python
    template_name.html
```
#### Шаг 10. Запуск Celery

```
Для Windows:
    celery -A mailganer worker -l info --pool=solo
    celery -A mailganer beat -l info 
```
