import asyncio
import json
import websockets
import requests
from DO.userDO import userDO
from DO.configDO import configDO


def evnet_sub(session_id):
    header = {
        'Authorization': 'Bearer ' + configDO.getAccess_token(),
        'Client-Id': configDO.getClient_id(),
        'Content-Type': 'application/json'
    }
    body = {
        "type": "stream.online",
        "version": "1",
        "condition": {"broadcaster_user_id": userDO.getId()},
        "transport": {
            "method": "websocket",
            "session_id": session_id
        }
    }
    print(header)
    print(body)
    response = requests.post('https://api.twitch.tv/helix/eventsub/subscriptions', headers=header, json=body)

    print(response.text)
    if response.status_code == 200:
        print("구독 완료")
    else:
        print("구독 실패")


def del_event_sub(session_id):
    header = {'Authorization': 'Bearer ' + configDO.getAccess_token(), 'Client-Id': configDO.getClient_id()}
    requests.delete('https://api.twitch.tv/helix/eventsub/subscriptions?id=' + session_id, headers=header)


async def connect():
    session_id = None
    try:
        print('connect실행')
        uri = "wss://eventsub.wss.twitch.tv/ws"
        async with websockets.connect(uri) as websocket:
            welcome_message = await websocket.recv()  # Welcome 메시지 수신
            welcome_message = json.loads(welcome_message)

            print(f"Welcome message: {welcome_message}")

            session_id = welcome_message['payload']['session']['id']

            evnet_sub(session_id)

            while True:
                message = await websocket.recv()  # 메시지 수신
                message = json.loads(message)

                if message['metadata']['message_type'] == 'notification':
                    print(f"Notification: {message}")
                elif message['metadata']['message_type'] == 'session_keepalive':
                    print("Keepalive message")
                elif message['metadata']['message_type'] == 'session_reconnect':
                    print(f"Reconnect: {message}")
                    # Reconnect 로직을 여기에 작성하실 수 있습니다.
                elif message['metadata']['message_type'] == 'revocation':
                    print(f"Revocation: {message}")
                    # Revocation 처리 로직을 여기에 작성하실 수 있습니다.
    except asyncio.CancelledError:
        print('연결 끊어짐')
        if session_id:  # session_id가 있을 때만 호출
            del_event_sub(session_id)
    return
