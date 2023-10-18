import re, sys, logging
from os import environ
from Script import script

logging.basicConfig(level=logging.ERROR)

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('BAC-0_1LttXwszpzeeYTV1_q35SD6Ezy5miRy1TLmSiAqCsnHZX0Q2G7YDsxluf_wPXcmt-3S8u7BEE_uHfpsmBIaFoaZiLajZMl5EvtIgQYmfVjK3-jIU_-H13EIqCU4oguoY2T8VuQOP-ZhCYN3Ml94btKD2OFhVYMF-310Xnk8lLgOIAmqg-Lu1IXRb6GucLxll8lbtbWuUjZymHd2gq1ZDw-maL7KUN9z_VuKwIFAtW1570-ySxDMufBsc_jfDAXS7qzlXmfKuhpJdBoA8wGgf3FRl5RvfWKQ_V3mHBcOmO_kl-9viz6nnrWkNpBiHJ-gqfRzcX1Yc58y5ENu3nbAAAAAWreVaUA', 'Auto_Filters_Bot')
API_ID = environ.get(''1747534 '')
if len(API_ID) == 0:
    logging.error('API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get(''5a2684512006853f2e48aca9652d83ea, '')
if len(API_HASH) == 0:
    logging.error('API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get(''6474315171:AAHxp_G0GK9TNd7JArBd4Uftd2xHVTisbGs, '')
if len(BOT_TOKEN) == 0:
    logging.error('BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Bot Admins
ADMINS = environ.get(''6087923109, '')
if len(ADMINS) == 0:
    logging.error('ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = environ.get(''-1001810601768, '').split()]
AUTH_CHANNEL = environ.get(''-1001910770735, '').split()]
LOG_CHANNEL = environ.get(''-1001826781136, '')
if len(LOG_CHANNEL) == 0:
    logging.error('LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# MongoDB information
DATABASE_URL = environ.get(''mongodb+srv://inyourdad007:UGJHdtBuhEUXgMt9@cluster0.jyb7ozn.mongodb.net/, "")
if len(DATABASE_URL) == 0:
    logging.error('DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/BongoBondhu_Bots')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/BongoBondhu_Bots')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "False")), False)
DELETE_TIME = int(environ.get('DELETE_TIME', 3600))
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/BongoBondhu_Bots")

# stream features vars
BIN_CHANNEL = environ.get("BIN_CHANNEL", "")
if len(BIN_CHANNEL) == 0:
    logging.error('BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "")
if len(URL) == 0:
    logging.error('URL is missing, exiting now')
    exit()
else:
    if URL.startswith('https://'):
        if not URL.endswith("/"):
            URL += '/'
    elif '.' in URL:
        URL = f'http://{URL}:{PORT}/'
    else:
        logging.error('URL is not valid, exiting now')
        exit()