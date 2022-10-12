# Инструкция по запуску

* Поместите .env файл для postgres в корень репозитория.
Существует .env.sample для postgres, можно использовать его.

* Поместите .env файл для django в папку test_drf. 
  Можно использовать .env.sample для django, который находится в папке test_drf,
  # ПЕРЕИМЕНОВАВ ЕГО В .env ПЕРЕД ЗАПУСКОМ docker-compose
Имена переменных для django: 
  DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, ALLOWED_HOST, SECRET_KEY

Если ввести команду в корне репозитория:

`sh env.sh && source run_app.sh`

То произойдёт следующее:
1. Будет создано новое виртуальное окружение.
2. Загружены зависимости.
3. Выполнена команда python3 manage.py collectstatic -c --no-input
4. docker-compose поднимет postgre + django uwsgi + nginx
 

При активации docker-compose миграция произойдёт внутри контейнера 
django uwsgi тогда, когда postgres будет готов принять соединение.

Проект в режиме DEBUG=True. При запуске проекта через скрипты вы увидите все логи.

Поднятие проекта требует времени, у меня загружается примерно за 3-4 минуты, 
благодарю вас за терпение.

Если вы не будете следовать автоматическому запуску, тогда:
 * Обязательно примените python3 manage.py collectstatic в папке test_drf, 
   чтобы загрузить статику до старта docker-compose
 * запустите docker-compose в корне репозитория

В корне репозитория файл openapi-schema.yml - Пользовательское представление API  формате OpenApi.

Фильтрация заказов: ?car_model__brand={int:pk}

Порядок заказов: ?ordering={amount|date}

Автотесты не написаны. Данные для тестирования не созданы.

Благодарю за внимание!