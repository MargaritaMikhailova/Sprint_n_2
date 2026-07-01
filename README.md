# Sprint_n_2


# Sprint_n_2 - Тестирование API для учебного сервиса «Доска»

Автотесты для API https://qa-desk.education-services.ru/

## Описание проекта

Проект содержит автоматизированные тесты для проверки API :
- Создание пользователя
- Логин польщователя
- Изменение объявления
- Создание объявления
- Удаление объявления

## Технологии

- **Python** 3.14.2
- **Pytest** 9.0.2
- **Allure** 2.38.1
- **Requests** 2.32.5

#### Запуск всех тестов
pytest tests/ -v

#### Запуск конкретного теста
- pytest tests/test_create_user.py -v
- pytest tests/test_login_user.py -v
- pytest tests/test_create_advert.py -v
- pytest tests/test_update_advert.py -v
- pytest tests/test_delete_advert.py -v

#### Открытие отчёта
allure open target/allure-report