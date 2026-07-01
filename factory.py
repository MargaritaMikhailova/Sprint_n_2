from faker import Faker
from data import Domain, USER_PASSWORD

fake = Faker()

class UserFactory:
    @staticmethod
    def create_user(faker):
        return {
            "email": fake.unique.email(domain=Domain.DOMAIN),
            "password": USER_PASSWORD,
            "submitPassword": USER_PASSWORD,
        }
