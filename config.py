from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 35660683))
        self.API_HASH = getenv("API_HASH", "7afb42cd73fb5f3501062ffa6a1f87f7")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8403356754:AAG0Y3kj8Zm4xPV-kOa-6hvpbkDemIiBdI8")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", -1002059929123))
        self.OWNER_ID = int(getenv("OWNER_ID", 7818323042))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "BQFLMyQASmxnF38miJivcan0D3xVnpECrkXM3kYmBKpCpPmUVO-KnP7_f_BrELkri1y-2BH8DpP3-SG6V0hvxdEfNvxsjQ740SoG-y5Dn4fQRpvVzsQGTrpglay5JezYqOHg3MqRpCpTcijV6vwaJJC0CRKPFiAGT7XeY8mPpwbkE729tewi7OOr53xEZrV8TbH27Asd1OLbZpGNWRODHEJyZE29Id6wtA6j7B-pLFUnDqldQJ4BpsDLihErX3OJGM8CSwJppJMnLYB9tTtKidMiLnkWGLDonfVsNcF_DUz2jWUgAD6JE9y4rX2iUmgi1Cv4ZAagqeJrjG47gAUVkZh1TDEbuQAAAAH17fm7AA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Senpai_Updates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/THE_DRAGON_SUPPORT")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
