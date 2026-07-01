import allure

from API_base import UserApi

class TestLoginUser:

    @allure.title('Успешная авторизация пользователя')
    def test_auth_user(self, user):
        login_response = UserApi.login_user(
            email=user["email"],
            password=user["password"]
        )
     
        assert login_response.status_code == 201
        assert "id" in login_response.json()["user"]
        assert login_response.json()["token"]["access_token"]
