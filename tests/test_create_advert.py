import allure
import pytest

from API_base import AdvertApi
from data import ADVERT, CATEGORIES

class TestCreateAdvert:

    @allure.title('Создание объявления с категорией {category}')
    @pytest.mark.parametrize("category", CATEGORIES)
    def test_create_advert(self, user, category):
        advert_data=ADVERT.copy()
        advert_data["category"] = category
 
        response_advert = AdvertApi.create_advert(
            token=user["token"],
            advert_data=advert_data,
        )
        assert response_advert.status_code == 201
        assert "id" in response_advert.json()