from user_queue import Admin
from load_env import GOOGLE_TOKEN

__all__ = ["BOT_CREATOR", "CAN_CREATE_QUEUES", "CHAT_IDS", "URLS", "MAX_QUEUE_SIZE"]

BOT_CREATOR = 1071609063

CAN_CREATE_QUEUES: dict[int, Admin] = {
    751586125: Admin(751586125, "Hu Tao", "Hu Tao"),
    731492287: Admin(731492287, "Masha", "🥰🥰староста🥰🥰"),
    406495448: Admin(406495448, "Egor", "Злобный клоун"),
    656638834: Admin(656638834, "Vika Nemolyaeva", "Lisa Malyaeva"),
    409428213: Admin(409428213, "Sergey Papikyan", "Ser Gey Papik(yan)"),
    433013981: Admin(433013981, "Danya", "Сахарный человек 🍭"),
    601351747: Admin(601351747, "Сергей Бородавко", "Боба"),
    344909548: Admin(344909548, "??", "??"),
    1071609063: Admin(1071609063, "Radmickey", "Mickey"),
    482676453: Admin(482676453, "Артём Худяков", "notxaa"),

}

CHAT_IDS = {-1001584422120: "03у26", -1001602645423: "04у26", -1001569727858: "00y27"}


def create_url(num: str):
    URL =  f"https://sheets.googleapis.com/v4/spreadsheets/" \
    f"1ZH7Wk0duy_11aK4ed6b10eNgQ0C_fr7V2ce86XlZixM/values/" \
    f"{num}!A:D?" \
    f"key={GOOGLE_TOKEN}"
    # print(URL)
    return URL

URLS = { -1001569727858: create_url("00")}
# -1001584422120: create_url("03"), -1001602645423: create_url("04"),

MAX_QUEUE_SIZE = 98 # why 98?

DEFAULT_QUEUE_SIZE = 25

MAX_QUEUE_NAME_LENGTH = 30