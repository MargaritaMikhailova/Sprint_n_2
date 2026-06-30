import allure

from message import ErrorMessage
from API_base import UserApi
from factory import UserFactory

class TestCreateUser:

    @allure.title('Успешная регстрация новго пользователя')
    def test_create_user_successful(self, faker):
        user_data = UserFactory.create_user(faker)

        create_resp = UserApi.create_user(
            email=user_data["email"],
            password=user_data["password"],
            submitPassword=user_data["password"]
        )
        assert create_resp.status_code == 201
        assert "id" in create_resp.json()["user"]


    @allure.title('Повторная регистрация пользователя')
    def test_create_duplicate_user(self, user):
        response_duplicate = UserApi.create_user(
            email=user["email"],
            password=user["password"],
            submitPassword=user["password"]
        )

        assert response_duplicate.status_code == 400
        assert response_duplicate.json()['message'] == ErrorMessage.LOGIG_ALERADY_EXIST
