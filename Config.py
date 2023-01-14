import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5888890044:AAGKsIyHZzgP7hDs6THZEcBkOJjgXL8XiQ4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKUBu4pbHBXP47jUPjv3iPnmUCTD-hBat4ZJG0HQEP6RhFFlze_0hlIs-mkuc_MSld7G2LayYULRPjcPLVzl30xNQe0Bqq6K41ZvOnZ-ieVDer77dy5oBeBxT10QOorP7AIz9JbBOoHaOq-JkHueYDVZ9ib5nrsnl2gqnTvKUHVh9KxZw-2wwlxa1SceH_tXuLJfS9Psrh5mLEPDDUxEXaa1NIlNBcut8cRWF22Dav2Y_rZ29W-o4W4fHBHeTjI5qri2BDOu7P8PxNpnzje0HqiJwzs-WXRUsCRwI_QejssOPq5Lt1EXoWQgrgJGZVql1oPlP0u4tX26c93eO_mCLZ49Aq4=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TRXOfficialRobot")
    SUPPORT = os.environ.get("SUPPORT", "xxxxxxxxxxxxxxdp")
    CHANNEL = os.environ.get("CHANNEL", "xxxxxxxxxxxxxxdp")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/5d9395aec555489708ef0.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5d9395aec555489708ef0.jpg")
