import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get this value from my.telegram.org/apps
API_ID = 10248430 #int(getenv("10248430"))
API_HASH = "42396a6ff14a569b9d59931643897d0d"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "6618122929:AAH3_xWlXb8Ye_VfbY8CxcJBSULz_KFef2U" #getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://gregorymjenson6:asdjdj@cluster0.0cu5abt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities

LOGGER_ID = -1001907436368 
LOG_GROUP_ID =-1001907436368
# Get this value from  on Telegram by /id
OWNER_ID = 6203163206

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/DNS-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SUKUNA_UPDATE_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Shizuka_update_group")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = "BQFx4q8AJY8DnBnTExgT6HYfFHJMa2Xk3fMKvbNC3oGqRfaD9GNpM_6yGPYSt_G-0aIyMepMVu5pWxdv2wZjoSEXvNn1JozBWM8QBt8TEs-y_UUpl76iGI1XQuo7-9EzW6ePrjAy9jEtcuiwM847nhGKMQo-5d8RDiHfpwa7r-QCekbcLnRszHcWdUN5YP8PBy2j2Vl9b6BRSZTiE2UL4ZHP7fpNyAZJLanGQNtV6QAFMZGviLTC6qj3Z9eOxYh7y7EwMPXSJVMlT0wPdiwImhl_at8pL6YCgC71MUMI1793e9NUKt0d2oTRUXj8lXYcuB-6xvQKRwagYhr4KFiIj3vzF8jVnQAAAAFPrvAtAA" #"BQCcYO4AOC7NPimTcvq7T6XfIiwMQxh9Z6XKRcV8ybMTiZXznqnOdfzpvAYQbCNsCOfWz31wR6pAjGecCP3nojlZOnaqUpbvDXuhQbHLgY9iHn_ikwbuZkUaOAWzBEnair1nZUzONb62bBgFR7XwhVVYhmkWxSHWfvBM6hALc-PkrT5SGBwL5Fz_XcXii5tHzB3UVw5ASkL2YXz9sCh5N2PdOAH8eOjPrWb5NL5wagRBm9kIcAbCIeED725GMCfGRmdvzbdYv9TiS_Q65Qp31KkXVST1Yov07cSd_c6Mh5ATG1t5zX3Ift43lu3-GS9vO0qLW0XZPnpH1ZOaQFFyo8sHXgra6wAAAAFyF4XTAA" #getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#    __      _______ _____    ___  __ _    _  _____ _____ _____   _____   ____ _______
#    \ \    / /_   _|  __ \   |  \/  | |  | |/ ____|_   _/ ____|  |  _ \ / __ \__   __|
#     \ \  / /  | | | |__) |  | \  / | |  | | (___   | || |       | |_) | |  | | | |
#      \ \/ /   | | |  ___/   | |\/| | |  | |\___ \  | || |       |  _ <| |  | | | |
#       \  /   _| |_| |       | |  | | |__| |____) |_| || |____   | |_) | |__| | | |
#        \/   |_____|_|       |_|  |_|\____/|_____/|_____\_____|  |____/ \____/  |_|


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/407b7c3930c1158f1492f.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/407b7c3930c1158f1492f.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
STATS_IMG_URL = "https://graph.org/file/407b7c3930c1158f1492f.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/eacfe007f9907f5854b10.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
