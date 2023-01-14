import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5888890044:AAGKsIyHZzgP7hDs6THZEcBkOJjgXL8XiQ4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJABu6EyT6qjyJ3-57fzBLwLGJMbYOqvmCalgLxXQXKrL6hypb8J6sFsfL5Gnbq-gVyrJJdX1JzdLNk821UK2e2Muxr4b_x_QNGSOU0CWca6t1JHvuAinP_PC8dTis8y-orqq__mvoRmV7DNWH-C44PAiF4YV-rnJWaATNILfLXAEZS1Vv2LoxxV8AqWL00SGwMsA7BVIWJj5jlg1WLkyMeFVDZWBaljcVdpvK2Y4u0mWMYmHlFvXNv2m8pQF3TGaj_9mer4rSlr92hVeKHK5awToQlu8Ag5lSC2iN4tBMGXAx1MbBxH8n-J2wZpL--B0f-PZ9qoNlabAhXEAfg3u0mLmSE=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TRXOfficialRobot")
    SUPPORT = os.environ.get("SUPPORT", "xxxxxxxxxxxxxxdp")
    CHANNEL = os.environ.get("CHANNEL", "xxxxxxxxxxxxxxdp")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/5d9395aec555489708ef0.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5d9395aec555489708ef0.jpg")
