# Тестовое задание Django + Stripe API бэкенд
# Данное приложение позволяет производить оплату товара через платежную систему Stripe
>Текст задания находится по [ссылке](https://github.com/MrKusaka/Django-Stripe/blob/master/Task.pdf)
### Копирование репозитория и установка зависимостей:
        git clone https://github.com/MrKusaka/djangoStripe
        cd djangoStripe
        virtualenv venv
        source venv/bin/activate
        pip install -r requirements.txt
### Устанавливаем переменные окружения:
>В папке djangoStripe создать файл .env и заполнить eго ключами

        SECRET_KEY=<secret_key>
        DEBUG=<debug>
> Ключи STRIPE_PUBLIC_KEY и STRIPE_SECRET_KEY необходимо взять по [ссылке](https://dashboard.stripe.com/test/apikeys) и добавить в settings:

        STRIPE_PUBLIC_KEY = "your API key"
        STRIPE_SECRET_KEY = "your API key"

### Применение миграций, создания суперпользователя и запуск проекта:
        python manage.py migrate
        python manage.py createsuperuser
        python manage.py runserver

### Импорт моей базы данных(прописывается в терминале):
        py manage.py loaddata items.json
>Добавил свои товары в базу данных, для того, чтобы можно было протестировать покупку, выглядит это так:
![img.png](img.png)
>(Вид на главной странице)

>Если продуктов нет, то будет следующий вид страницы:
![img_1.png](img_1.png)
(Это функция так же добавлена для тестирования)

> Ссылка направляет нас в Admin, для создания продукта(item):
![img_2.png](img_2.png)
> После создания, необходимо вернуться на главную страницу, нажав справа вверху кнопку "Открыть сайт"