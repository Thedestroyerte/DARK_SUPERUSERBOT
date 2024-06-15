import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from ... import app, SUDO_USER
from ... import *

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@app.on_message(cdz(["alive"])  & (filters.me | filters.user(SUDO_USER)))
async def alive(client: Client, message: Message):
    r = await message.reply_text("**#FEEL_4ST**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"︎ ™°‌ #UR_DADDY_4ST_HERE_ ︎︎︎\n\n"
        f"🇻ᗴᖇՏIOᑎ ⁂1.0\n"
        f"🇵Iᑎᘜ ⁂ {ping * 1000:.3f}ᴍs\n"
        f"🇺ᑭTIᗰᗴ ⁂ {uptime}\n"
        f"🇵YTᕼOᑎ ⁂ {python_version()}`\n"
        f"🇵YᖇOᘜᖇᗩᗰ ⁂ {__version__}\n"
        f"👑‌🇴Oᗯᑎᗴᖇ💗 ⁂ {client.me.mention}"    
    )

@app.on_message(cdz(["ping"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**™°‌ #FEEL_4ST**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f" ™°‌ #⚡𝖸𝖮𝖴𝖱_𝖣𝖠𝖣𝖸_𝖣𝖠𝖱𝖪_𝖧𝖤𝖱𝖤⚡ \n\n"
        f"🇵𝖨𝖭𝖦  ⁂ {ping * 1000:.3f}ᴍs\n"
        f"🇹𝖨𝖬𝖤  ⁂ {uptime}\n"
        f"⚡🇸𝖴𝖯𝖤𝖱 🇴𝖶𝖭𝖤𝖱⚡ ⁂ {client.me.mention}\n"
              )
@app.on_message(cdz(["repo"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐑ᴇᴘᴏ**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"𝗥𝗘𝗣𝗢 ⁂\n\n"
        f"[💫 𝐑ᴇᴘᴏ 💫](https://github.com/Thedestroyerte/DARK_SUPERUSERBOT)\n"
    )    


__NAME__ = " Aᴄᴛɪᴠᴇ "
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**

`.alive` - **Check Ping Latency
Of Your Userbot Server.**

`.repo` - **chek bot repo.**
"""
