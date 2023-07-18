import json
import requests
from DO.configDO import configDO
import time


def set_tokken():
    with open('config.json', 'r') as f:
        config = json.load(f)
        configDO.setClient_id(config['client_id'])
        configDO.setClient_secret(config['client_secret'])
        configDO.setAccess_token(config['access_token'])
        configDO.setExpires_at(config["expires_at"])

        header = {'Authorization': 'OAuth ' + configDO.getAccess_token()}
        response = requests.get('https://id.twitch.tv/oauth2/validate', headers=header)
        print(response.text)

    if configDO.getAccess_token() is None or configDO.getExpires_at() < time.time():
        print("토큰 존재하지 않음")
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        req_data = {'client_id': configDO.getClient_id(), 'client_secret': configDO.getClient_secret(),
                    'grant_type': 'client_credentials'}
        response = requests.post('https://id.twitch.tv/oauth2/token', headers=headers, data=req_data)

        if response.status_code == 200:
            print("토큰 발급 성공")
            response = response.json()
            configDO.setAccess_token(response["access_token"])
            configDO.setExpires_at(time.time() + response["expires_in"])
            configDO.write_config()
        else:
            print("토큰 발급 에러")

    else:
        print("토큰 존재함")
