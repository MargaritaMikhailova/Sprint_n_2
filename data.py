

class Urls:
    MAIN_URL = "https://qa-desk.education-services.ru"

class EndPoint:
    USER = "/api/signup"
    USER_LOGIN = "/api/signin"
    CREATE_ADVERT = '/api/create-listing'
    UPDATE_ADVERT = '/api/update-offer/{id}'
    DELETE_ADVERT = '/api/listings/{id}'

class Domain:
    DOMAIN = "mail.com"

ADVERT = {
    'name': 'test',
    'category': "Садоводство",
    'condition': 'Новый',
    'city': 'Москва',
    'description': 'test1',
    'price': '1000'
        }


CATEGORIES = ["Авто", "Книги", "Садоводство", "Хобби", "Технологии"]

USER_PASSWORD = "Aa12345!"