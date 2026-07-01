import allure

from data import ADVERT
from API_base import AdvertApi
from message import ErrorMessage

class TestUpdateAdvert:

    @allure.title('Успешное редактирование любого объявления')
    def test_update_advert(self, user, advert):
        response_advert = AdvertApi.update_advert(
            token=user["token"],
            advert_data=ADVERT.copy(),
            id=advert["id"]
        )
        assert response_advert.status_code == 200
        assert "id" in response_advert.json()

    @allure.title('Редактирование объявление созданное не тем пользователем, которым авторизован')
    def test_not_update_advert(self, user, other_user_advert):
        response_advert = AdvertApi.update_advert(
            token=user["token"],
            advert_data=ADVERT.copy(),
            id=other_user_advert
        )
        assert response_advert.status_code == 401
        assert "error" in response_advert.json()
        assert response_advert.json()['message'] == ErrorMessage.ADVERT_NOT_UPDATE

  
