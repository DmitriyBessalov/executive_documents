## Срез проекта формирования документации на GraphQL

### Запуск ### 

    python3 main.py
    cd /var/www/executive-journal-service
    poetry shell
    poetry update package

# Миграции #
### Сгенирировать миграцию ###
alembic revision --autogenerate -m "TIMESTAMP"

### Применить последнию миграцию ###
alembic upgrade head