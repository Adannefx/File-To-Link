#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"@Anime_X_hunters_bot is a Telegram Bot for storing posts or files that can be accessed via a special link.\n\n• Creator: @Its_Tartaglia_Childe\n• Framework: Pyrograms\n• Channel : @Animes_X_Hunters\n\n👨‍💻 Developed by @Animes_X_Hunters",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥​ᴄʟᴏꜱᴇ​💥", callback_data="close"),
                        InlineKeyboardButton("⚡ᴀʙᴏᴜᴛ⚡", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>Hi there this is a file store bot which is convert any file to link...\nthen you can access this file through a specific link...!\n\nCreator - <a href=https://t.me/Its_Tartaglia_Childe>'>SAHIL</a>\nMy Channel - <a https://t.me/Anime_X_Hunters>Anime Hunters</a>\nDicsussion Group - <a https://t.me/Hunters_Discussion>Hunters Discussion</a>\n\n👨‍💻 Developed by @Its_Tartaglia_Childe</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥​ᴄʟᴏꜱᴇ​💥", callback_data="close"),
                        InlineKeyboardButton("🚀ʜᴇʟᴘ🚀", callback_data="help")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
