import os
from pydrive2.auth import GoogleAuth
from bot.helpers.cookies import get_cookies

currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)


class TG_CONFIG:
    api_id = "26910777"

    api_hash = "8601f2f24993f6fdbcbac3bb27ceec38"

    bot_token = "7600596195:AAHDddWPPK5OzQFXbisolzoxo24YbCthdhk"

    #DEVS or #OWNERS
    sudo_users = [5232142502, 6991688781]

    session = "1BVtsOKEBu5oEgfB2oT4irQrOUG101RAVWmMomsZqa9P9qSwvKORwfkeSosR4i9R1r7Uhb7Esutzjf_345UgMMj8eCcaD26q7OOsKhOG0HA-YDaZLVNIW14zx5X68tujJ7IFLLzZ2LXmrt4nB6dVXTMprSujFfcwOZJEhdrtXXE61YkAbmMRj0-Z4ccDjLRz6WPZn3oVswnOyDSqzM07KzAhfEfXMrNO9BSeZrj8I-G0NLFCRbq2R2QoD9NK55iES1oHvOXKyBbfqmbjMR0DgoEl_86xZgaUFFucSyKIwLO3Ci1xE4wT8jNXhS1CSyvN23QcLL_59t62bOlIqdpFNATALm9zP3Ic="

    bot_creater = "AJ_TVSERIAL"  # Don't Remove if you Respect the DEV

    bot_creater_id = "@AJ_TVSERIAL"  # Don't Remove if you Respect the DEV


class UPLOAD_CONGIF:
    upload_to = "gdrive" #tg, ftp, gdrive
    default_upload_to = "tg"


class GDRIVE_CONFIG:
    #for Gdrive (Leave it as Empty String if not Gdrive Upload is turned ON)
    root_folder_id = ""

    #keep it empty if you don't have index link or don't touch
    indexlink_format = "https://example.workers.dev/0:/{}/{}"

    is_making_drive_files_public = True


class GD_SHARER_CONFIG:

    is_uploading_to_filepress = False

    #Don't add a trailing slash at the end (keep in this format only - https://new5.filepress.store)
    filepress_url = "https://new9.filepress.store"
    
    cookie_path = dirPath + "/cookies/filepress.txt"
    _, dict_cookies = get_cookies(cookie_path)
    
    filepress_connect_sid_cookie_value = dict_cookies.get("connect.sid")


class PROXY_CONFIG:
    #Keep it as a empty string if you don't have proxy
    proxy_url = ""
    USE_PROXY_WHILE_DOWNLOADING = False


class FTP_CONFIG:
    #FTP Creds
    ftp_url = ""

    ftp_domain = ""
    
    ftp_user = ""
    
    ftp_password = ""


class FILENAME_CONFIG:

    filename_format = "p2p"  # p2p or non-p2p

    p2p_audio_bitrate = "K"

    non_p2p_audio_bitrate = "Kbps"

    underscore_before_after_group_tag = "__"

    language_order = ['hi', 'ta', 'te', 'bn', 'gu', 'pa', 'as', 'or',
                    'ml', 'mr', 'kn', 'th', 'ja', 'th', 'id', 'ms', 'ko', 'bho', 'bh', 'en']

    default_group_tag = "RV" # Don't change it if you Respect the DEV

    #Dict made to add Group Tag according to the user requesting to DL (according to there TG ID) if not in list then takes the default_group_tag
    group_tag_mapping = {
        '6991688781': 'AT',
        '5232142502' : 'AJ'
    }


DL_DONE_MSG = """
✅ <b> Task Completed In </b> <code>{}</code>

<b>FileName : </b> <code>{}</code>
<b>OTT : </b> <code>{}</code>
<b>Size : </b> <code>{}</code>
"""


START_MSG = """
<b>Hello <code>@{}</code>,
 I am one and only DRM Downloader Bot on Telegram.

I can help you to download content from OTT Platforms

You can use me to Download DRM protected links to Telegram & Google Drive

Here I support a vast number of otts from where you can download Drm or non-drm videos easily..

If You Found Any Issue Contact Support<a href='https://t.me/Dangal_bhai'>⏤͟͟͞͞ 🇮🇳 𝐀𝐧𝐢𝐤𝐞𝐭 𝐂𝐨𝐝𝐞𝐫 ᯤ̸</a> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴛʀɪᴀʟ.
</b>

> <code>{}</code>

<b>Made by @AJ_TVSERIAL</b>
"""

SIMPLE_CAPTION = '''<code>{}</code>'''

LOG_MESSAGE = "<code>[+]</code> <b>{}</b>\n<b><code>[+]</code> <b>{} : </b><code>{}</code>"


proxies = {
    "https": PROXY_CONFIG.proxy_url,
    "http": PROXY_CONFIG.proxy_url
} if PROXY_CONFIG.proxy_url and PROXY_CONFIG.proxy_url.strip() else None

tplay_path = os.path.join(
    dirPath, "static", "tplay.json")

languages_info_file_path = os.path.join(
    dirPath, "static", "languages_info.json")

client_secrets_json = os.path.join(dirPath, "static", "client_secrets.json")

token_file = os.path.join(dirPath, "static", "session")

dl_folder = os.path.join(dirPath, "downloads")  

os.makedirs(dl_folder) if not os.path.exists(dl_folder) else None

iswin = 1 if os.name == "nt" else 0


if iswin == 0:
    aria2c = dirPath + "/binaries/aria2c"
    mp4decrypt = dirPath + "/binaries/mp4decrypt"
    ytdlp = dirPath + "/binaries/yt-dlp"

    os.system(f"chmod 777 {aria2c} {mp4decrypt} {ytdlp}")
else:
    aria2c = dirPath + "/binaries/aria2c.exe"
    mp4decrypt = dirPath + "/binaries/mp4decrypt.exe"
    ytdlp = dirPath + "/binaries/yt-dlp.exe"


gauth = GoogleAuth()
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_secrets_json
