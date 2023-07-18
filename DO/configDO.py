import json


class configDO:
    __instance = None
    __client_id = None
    __client_secret = None
    __access_token = None
    __expires_at = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self, client_id=None, client_secret=None, access_token=None, expires_at=None):
        if self.__instance is not None:
            raise ValueError("An instantiation already exists!")
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__access_token = access_token
        self.__expires_at = expires_at

    def setClient_id(self, data):
        self.__client_id = data

    def setClient_secret(self, data):
        self.__client_secret = data

    def setAccess_token(self, data):
        self.__access_token = data

    def setExpires_at(self, data):
        self.__expires_at = data

    def getClient_id(self):
        return self.__client_id

    def getClient_secret(self):
        return self.__client_secret

    def getAccess_token(self):
        return self.__access_token

    def getExpires_at(self):
        return self.__expires_at

    def write_config(self):
        data = {
            'client_id': self.__client_id,
            'client_secret': self.__client_secret,
            'access_token': self.__access_token,
            'expires_at': self.__expires_at
        }
        with open('config.json', 'w') as f:
            json.dump(data, f)


configDO = configDO.get_instance()
