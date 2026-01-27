# REQUIRED CONFIG
BOT_TOKEN = "8212814456:AAEyijOk7aKhW5y6g1kGW6S8I02sz0ozo7w"
OWNER_ID = 8557029592
TELEGRAM_API = 31355944
TELEGRAM_HASH = "167e960d46363e3098f9c1fc78496adb"
DATABASE_URL = "mongodb+srv://botskingdom2:t7ognZuINrNfH3tj@cluster0.ystdy4m.mongodb.net/?retryWrites=true&w=majority"

# OPTIONAL CONFIG
DEFAULT_LANG = "en"
TG_PROXY = (
    {}
)  # {"scheme": ”socks5”, "hostname": ””, "port": 1234, "username": ”user”, "password": ”pass”}
USER_SESSION_STRING = ""
CMD_SUFFIX = "1"
AUTHORIZED_CHATS = "-1003546488840"
SUDO_USERS = ""
STATUS_LIMIT = 10
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SWAP = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# Hyper Tg Downloader
HELPER_TOKENS = ""

# MegaAPI v4.30
MEGA_EMAIL = ""
MEGA_PASSWORD = ""

# Disable Options
DISABLE_TORRENTS = False
DISABLE_LEECH = False
DISABLE_BULK = False
DISABLE_MULTI = False
DISABLE_SEED = False
DISABLE_FF_MODE = False

# Telegraph
AUTHOR_NAME = "HemanthBot"
AUTHOR_URL = "http://t.me/ALONEKINGSTAR77"

# Task Limits
DIRECT_LIMIT = 0
MEGA_LIMIT = 0
TORRENT_LIMIT = 0
GD_DL_LIMIT = 0
RC_DL_LIMIT = 0
CLONE_LIMIT = 0
JD_LIMIT = 0
NZB_LIMIT = 0
YTDLP_LIMIT = 0
PLAYLIST_LIMIT = 0
LEECH_LIMIT = 0
EXTRACT_LIMIT = 0
ARCHIVE_LIMIT = 0
STORAGE_LIMIT = 0

# Insta video downloader api
INSTADL_API = ""

# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""

# Media Search
IMDB_TEMPLATE = """<b>Title: </b> {title} [{year}]
<b>Also Known As:</b> {aka}
<b>Rating ⭐️:</b> <i>{rating}</i>
<b>Release Info: </b> <a href="{url_releaseinfo}">{release_date}</a>
<b>Genre: </b>{genres}
<b>IMDb URL:</b> {url}
<b>Language: </b>{languages}
<b>Country of Origin : </b> {countries}

<b>Story Line: </b><code>{plot}</code>

<a href="{url_cast}">Read More ...</a>"""

# Task Tools
FORCE_SUB_IDS = ""
MEDIA_STORE = True
DELETE_LINKS = False
CLEAN_LOG_MSG = False

# Limiters
BOT_MAX_TASKS = 0
USER_MAX_TASKS = 0
USER_TIME_INTERVAL = 0
VERIFY_TIMEOUT = 0
LOGIN_PASS = ""

# Bot Settings
BOT_PM = False
SET_COMMANDS = True
TIMEZONE = "Asia/Kolkata"

# GDrive Tools
GDRIVE_ID = ""
GD_DESP = "Uploaded with HemanthBot"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# YT Tools
YT_DESP = "Uploaded to YouTube by HemanthBot bot"
YT_TAGS = ["telegram", "bot", "youtube"]  # or as a comma-separated string
YT_CATEGORY_ID = 22
YT_PRIVACY_STATUS = "unlisted"

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
SHOW_CLOUD_LINK = True
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# JDownloader
JD_EMAIL = ""
JD_PASS = ""

# Sabnzbd
USENET_SERVERS = []

# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
UPDATE_PKGS = True

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
USER_TRANSMISSION = True
HYBRID_LEECH = True
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_CAPTION = ""
THUMBNAIL_LAYOUT = ""

# Log Channels
LEECH_DUMP_CHAT = ""
LINKS_LOG_ID = "-1003409524277"
MIRROR_LOG_ID = "-1003409524277"

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 0
WEB_PINCODE = True

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
