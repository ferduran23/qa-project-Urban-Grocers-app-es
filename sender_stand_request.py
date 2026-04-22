import requests
import configuration
import data


def post_new_user(user_body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body
    )
    return response


def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )
    return response


def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json()["authToken"]