import requests

from data import Urls, EndPoint
from requests_toolbelt import MultipartEncoder

class UserApi:

    @staticmethod
    def create_user(*, email: str, password: str, submitPassword: str):
        payload = {"email": email, "password": password, "submitPassword": submitPassword}
        return requests.post(f"{Urls.MAIN_URL}{EndPoint.USER}", json=payload, timeout=30)

    @staticmethod
    def login_user(*, email: str, password: str):
        payload = {"email": email, "password": password}
        return requests.post(f"{Urls.MAIN_URL}{EndPoint.USER_LOGIN}", json=payload, timeout=30)
    
class AdvertApi:

    @staticmethod
    def create_advert(*, token: str, advert_data: dict):
        encoder = MultipartEncoder(advert_data)
        headers = {"Authorization": f"Bearer {token}", 'Content-Type': encoder.content_type}
        return requests.post(f"{Urls.MAIN_URL}{EndPoint.CREATE_ADVERT}", data=encoder, headers=headers, timeout=30)
            
    @staticmethod
    def update_advert(*, token: str, advert_data: dict, id: str):
        encoder = MultipartEncoder(advert_data)
        headers = {"Authorization": f"Bearer {token}", 'Content-Type': encoder.content_type}
        return requests.patch(f"{Urls.MAIN_URL}{EndPoint.UPDATE_ADVERT.format(id=id)}", data=encoder, headers=headers, timeout=30)
    
    @staticmethod
    def delete_advert(*, token: str, id: str):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.delete(f"{Urls.MAIN_URL}{EndPoint.DELETE_ADVERT.format(id=id)}", headers=headers, timeout=30)