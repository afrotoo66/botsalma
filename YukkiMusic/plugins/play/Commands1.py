import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from YukkiMusic import check_client


@app.on_callback_query(filters.regex("ddd"))
async def dddf(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""\n\n\n╭── • [salma music](t.me/UI_VM) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **سلمي شغلي + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **سلمي طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **سلمي الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **سلمي اص** او **اسكتي**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **سلمي تكلمي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **سلمي ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **سلمي كملي** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [salma music](t.me/UI_VM) • ──╯""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/so_alfaa")
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "ᯓ 𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌♬⁩", callback_data="fft"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )

@app.on_callback_query(filters.regex("sop"))
async def sop(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚂𝙾𝚄𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 𓁘\n✧ 𝑱𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑴𝒊𝒓𝒂 𝑻𝒐 𝑺𝒆𝒆 𝑨𝒍𝒍 𝑼𝒑𝒅𝒂𝒕𝒆\n\n- 𝑴𝒂𝒔𝒕𝒆𝒓 -› @IIUll_l\n- 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 -› @UI_VM""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UI_VM")
                ],[
                    InlineKeyboardButton(
                        "ᯓ 𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌♬⁩", callback_data="am"),
                    InlineKeyboardButton(
                        "◌ᴅᴇᴠᴇʟᴏᴘᴇʀ◌", url=f"t.me/IIUll_l")
                ],[

                    InlineKeyboardButton(
                        "رجوع", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )
