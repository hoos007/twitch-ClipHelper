import requests


def get_token_req():
    url = "https://id.twitch.tv/oauth2/token"
    data = {"client_id": "", "client_secret": "", "grant_type": "client_credentials"}
    headers = {"Content-Type": "Content-Type: application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        print("토큰 발급 성공")
    else:
        print("토큰 발급 에러")

    response = response.json()

    token = response["access_token"]
    expires_in = response["expires_in"]

    return token, expires_in
