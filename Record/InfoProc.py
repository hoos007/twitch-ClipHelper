from API.api import user_info, channel_info
from DO.userDO import userDO


def search_info(search):
    user_info(search)
    channel_info(userDO.getId())
    return None
