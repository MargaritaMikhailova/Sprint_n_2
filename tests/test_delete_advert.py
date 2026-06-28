import allure


from API_base import AdvertApi
from message import ErrorMessage

class TestDeleteAdvert:

    @allure.title('Успешное удаление объявления')
    def test_delete_advert(self, user, advert):
        response_advert = AdvertApi.delete_advert(
            token=user["token"],
            id=advert["id"]
        )
        assert response_advert.status_code == 200
        assert response_advert.json()['message'] == ErrorMessage.DELETE_ADVERT
        
