
from bot_config import Config
from plugins.responses import Response
import pyrogram
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client as Bot
import re

@Bot.on_message(filters.private & filters.regex(pattern="((سلام)|(slm)|(salam)|(hi)|(hello))$",flags=re.I))
async def say_hello(bot: Bot, message: Message):
    await message.reply(text=Response.Hello, quote=True)
    await message.reply(text=Response.WhatsUp)


@Bot.on_message(filters.group & filters.command("all",prefixes=['!','/',':']))
async def mention_all_members(bot: Bot, message: Message):
    members = await message.chat.get_members()
    mention_text = ", ".join(member.user.mention(
        member.user.first_name) for member in members)
    await message.reply(text=mention_text, quote=True)


@Bot.on_message(filters.user(["BotFather"]) & filters.command("history count",prefixes=['!','/',':']))
async def get_chat_history_count(bot: Bot, message: Message):
    n = await bot.get_history_count(message.chat.id)
    print(n)
    await message.reply(text=n)


@Bot.on_message( filters.command("myid",prefixes=['!','/',':']))
async def get_chat_id(bot: Bot, message: Message):
    await message.reply(text=message.chat.id, quote=True)

