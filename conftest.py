import pytest

from factory import UserFactory
from API_base import UserApi, AdvertApi
from data import ADVERT

@pytest.fixture
def user(faker):
    user_data = UserFactory.create_user(faker)

    create_resp = UserApi.create_user(
        email=user_data["email"],
        password=user_data["password"],
        submitPassword=user_data["submitPassword"],
    )

    login_resp = UserApi.login_user(
        email=user_data["email"],
        password=user_data["password"],
    )
    token = login_resp.json()["token"]["access_token"]
    id_user = login_resp.json()["user"]["id"]

    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "token": token,
        "create_response": create_resp,
        "id": id_user, 
    }



@pytest.fixture
def advert(user):
    advert_data = ADVERT.copy()

    create_advert = AdvertApi.create_advert(
        token=user["token"], 
        advert_data=advert_data
        )

    data_advert = {
        "name": create_advert.json()["name"], 
        "category": create_advert.json()["category"],
        "condition": create_advert.json()["condition"],
        "city": create_advert.json()["city"],
        "description": create_advert.json()["description"],
        "price": create_advert.json()["price"],
        "id": create_advert.json()["id"]
    } 

    yield data_advert

    AdvertApi.delete_advert(
        token=user["token"],
        id=str(data_advert["id"])
    )

    

@pytest.fixture
def other_user_advert(faker):
    user_data = UserFactory.create_user(faker)

    UserApi.create_user(
        email=user_data["email"],
        password=user_data["password"],
        submitPassword=user_data["submitPassword"],
    )
    login_resp = UserApi.login_user(
        email=user_data["email"],
        password=user_data["password"],
    )
    token = login_resp.json()["token"]["access_token"]

    create_advert = AdvertApi.create_advert(
        token=token,
        advert_data=ADVERT.copy(),
    )

    advert_id = create_advert.json()["id"]

    yield advert_id

    AdvertApi.delete_advert(
        token=token, 
        id=str(advert_id)
    )
