import requests
from DO.configDO import configDO
from DO.userDO import userDO
from DO.channelDO import channelDO


def user_info(userid):
    headers = {'Authorization': 'Bearer ' + configDO.getAccess_token(), 'Client-Id': configDO.getClient_id()}
    response = requests.get('https://api.twitch.tv/helix/users?login=' + userid, headers=headers)

    if response.status_code == 200:
        print("유저 정보 요청 성공")
        response = response.json()
        print(response)
        userDO.setBroadcaster_type(response['data'][0]['broadcaster_type'])
        userDO.setCreated_at(response['data'][0]['created_at'])
        userDO.setDescription(response['data'][0]['description'])
        userDO.setDisplay_name(response['data'][0]['display_name'])
        userDO.setId(response['data'][0]['id'])
        userDO.setLogin(response['data'][0]['login'])
        userDO.setOffline_image_url(response['data'][0]['offline_image_url'])
        userDO.setProfile_image_url(response['data'][0]['profile_image_url'])
        userDO.setType(response['data'][0]['type'])
        userDO.setView_count(response['data'][0]['view_count'])
    else:
        print("유저 정보 요청 실패")


def channel_info(id):
    headers = {'Authorization': 'Bearer ' + configDO.getAccess_token(), 'Client-Id': configDO.getClient_id()}
    response = requests.get('https://api.twitch.tv/helix/channels?broadcaster_id=' + id, headers=headers)

    if response.status_code == 200:
        print("채널 정보 요청 성공")
        response = response.json()
        print(response)
        channelDO.setBroadcaster_id(response['data'][0]['broadcaster_id'])
        channelDO.setBroadcaster_login(response['data'][0]['broadcaster_login'])
        channelDO.setBroadcaster_name(response['data'][0]['broadcaster_name'])
        channelDO.setBroadcaster_language(response['data'][0]['broadcaster_language'])
        channelDO.setGame_id(response['data'][0]['game_id'])
        channelDO.setGame_name(response['data'][0]['game_name'])
        channelDO.setTitle(response['data'][0]['title'])
        channelDO.setDelay(response['data'][0]['delay'])
        channelDO.setTags(response['data'][0]['tags'])
    else:
        print("채널 정보 요청 실패")


def load_image_from_url(url):
    response = requests.get(url)
    img_data = response.content
    return img_data
