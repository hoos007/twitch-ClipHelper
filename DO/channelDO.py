class channelDO:
    __instance = None
    __broadcaster_id = None
    __broadcaster_login = None
    __broadcaster_name = None
    __broadcaster_language = None
    __game_id = None
    __game_name = None
    __title = None
    __delay = None
    __tags = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self, broadcaster_id = None, broadcaster_login = None, broadcaster_name = None, broadcaster_language = None, game_id = None, game_name = None,
                 title = None, delay = None, tags = None):
        if self.__instance is not None:
            raise ValueError("An instantiation already exists!")
        self.__broadcaster_id = broadcaster_id
        self.__broadcaster_login = broadcaster_login
        self.__broadcaster_name = broadcaster_name
        self.__broadcaster_language = broadcaster_language
        self.__game_id = game_id
        self.__game_name = game_name
        self.__title = title
        self.__delay = delay
        self.__tags = tags

    def setBroadcaster_id(self, data):
        self.__broadcaster_id = data

    def setBroadcaster_login(self, data):
        self.__broadcaster_login = data

    def setBroadcaster_name(self, data):
        self.__broadcaster_name = data

    def setBroadcaster_language(self, data):
        self.__broadcaster_language = data

    def setGame_id(self, data):
        self.__game_id = data

    def setGame_name(self, data):
        self.__game_name = data

    def setTitle(self, data):
        self.__title = data

    def setDelay(self, data):
        self.__delay = data

    def setTags(self, data):
        self.__tags = data

    def getBroadcaster_id(self):
        return self.__broadcaster_id

    def getBroadcaster_login(self):
        return self.__broadcaster_login

    def getBroadcaster_name(self):
        return self.__broadcaster_name

    def getBroadcaster_language(self):
        return self.__broadcaster_language

    def getGame_id(self):
        return self.__game_id

    def getGame_name(self):
        return self.__game_name

    def getTitle(self):
        return self.__title

    def getDelay(self):
        return self.__delay

    def getTags(self):
        return self.__tags


channelDO = channelDO.get_instance()
