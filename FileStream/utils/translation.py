from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Hᴇʏ, </b>{}\n 
<b>I'ᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏs/ғɪʟᴇs ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ 😈</b>\n
<b>Just Send me Any Video/PDF and See My Magic 😃</b>\n
<b>💕 @{}</b>\n"""

    HELP_TEXT = """
<b>- sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴍᴇᴅɪᴀ</b>
<b>- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ</b>\n
<b>🔞 𝗔𝗱𝘂𝗹𝘁 Video Bhejana toh Tere hi Gend ke Ched mein Lond ghusa dunga 💀</b>\n
<i><b> ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ <a href='https://telegram.me/TEAM_OPTECH'>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b></i>"""

    ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : {}</b>\n
<b>✦ ᴠᴇʀsɪᴏɴ : {}</b>
<b>✦ ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ : 2014</b>
<b>✦ ᴍᴇʀᴀ ʙᴀᴀᴘ 🙏 : <a href='https://telegram.me/HACKHEISTBOT'>HACKHEIST</a></b>\n
"""

    STREAM_TEXT = """
<i><u>𝗟𝗲 𝗧𝗲𝗿𝗶 𝗟𝗶𝗻𝗸 🥰</u></i>\n
<b>📂 ʙᴀɴᴅɪ ᴋᴀ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 ʙᴀɴᴅɪ ᴋᴀ ᴡᴇɪɢʜᴛ :</b> <code>{}</code>\n
<b>📥 ᴘᴀᴛᴀɴᴇ ᴋᴀ ᴍᴇᴛʜᴏᴅ :</b> <code>{}</code>\n
<b>🖥 ᴘᴀᴛᴀɴᴇ ᴋᴇ ʙᴀᴀᴅ :</b> <code>{}</code>\n
<b>🔗 ᴋʜᴏᴛᴀ ᴋʜᴜᴅᴀɪ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>𝗟𝗲 𝗧𝗲𝗿𝗶 𝗟𝗶𝗻𝗸 🥰</u></i>\n
<b>📂 ʙᴀɴᴅɪ ᴋᴀ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 ʙᴀɴᴅɪ ᴋᴀ ᴡᴇɪɢʜᴛ :</b> <code>{}</code>\n
<b>📥 ᴘᴀᴛᴀɴᴇ ᴋᴀ ᴍᴇᴛʜᴏᴅ :</b> <code>{}</code>\n
<b>🖥 ᴘᴀᴛᴀɴᴇ ᴋᴇ ʙᴀᴀᴅ :</b> <code>{}</code>\n
<b>🔗 ᴋʜᴏᴛᴀ ᴋʜᴜᴅᴀɪ :</b> <code>{}</code>\n"""


    BAN_TEXT = "**__ʙʜᴀᴋ ʙsᴅᴋ, ʙᴀɴ ᴋᴀʀᴅɪʏᴀ ʜᴜ sᴏᴄʜɴᴀ ʙʜɪ ᴍᴀᴀᴛ ᴋɪ ᴜɴʙᴀɴ ᴋᴀʀᴅᴜɴɢᴀ 🤬.__\n\n**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ᴍᴀᴅᴀᴅ', callback_data='help'),
            InlineKeyboardButton('ᴊᴀᴀɴᴋᴀʀᴏ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦 🥰", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦 🥰", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 🥰", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
