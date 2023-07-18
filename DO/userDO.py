class userDO:
    __instance = None
    __broadcaster_type = None
    __created_at = None
    __description = None
    __display_name = None
    __id = None
    __login = None
    __offline_image_url = None
    __profile_image_url = None
    __type = None
    __view_count = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self, broadcaster_type=None, created_at=None, description=None, display_name=None, id=None, login=None,
                 offline_image_url=None, profile_image_url=None, type=None, view_count=None):
        if self.__instance is not None:
            raise ValueError("An instantiation already exists!")
        self.__broadcaster_type = broadcaster_type
        self.__created_at = created_at
        self.__description = description
        self.__display_name = display_name
        self.__id = id
        self.__login = login
        self.__offline_image_url = offline_image_url
        self.__profile_image_url = profile_image_url
        self.__type = type
        self.__view_count = view_count

    def setBroadcaster_type(self, data):
        self.__broadcaster_type = data

    def setCreated_at(self, data):
        self.__created_at = data

    def setDescription(self, data):
        self.__description = data

    def setDisplay_name(self, data):
        self.__display_name = data

    def setId(self, data):
        self.__id = data

    def setLogin(self, data):
        self.__login = data

    def setOffline_image_url(self, data):
        self.__offline_image_url = data

    def setProfile_image_url(self, data):
        self.__profile_image_url = data

    def setType(self, data):
        self.__type = data

    def setView_count(self, data):
        self.__view_count = data

    def getBroadcaster_type(self):
        return self.__broadcaster_type

    def getCreated_at(self):
        return self.__created_at

    def getDescription(self):
        return self.__description

    def getDisplay_name(self):
        return self.__display_name

    def getId(self):
        return self.__id

    def getLogin(self):
        return self.__login

    def getOffline_image_url(self):
        return self.__offline_image_url

    def getProfile_image_url(self):
        return self.__profile_image_url

    def getType(self):
        return self.__type

    def getView_count(self):
        return self.__view_count


userDO = userDO.get_instance()
