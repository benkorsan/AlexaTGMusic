# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma



import asyncio
import random
import time
from sys import version as pyver
from typing import Dict, List, Union

import psutil
from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Alexa import ASSIDS, BOT_ID, MUSIC_BOT_NAME, OWNER_ID, SUDOERS, app
from Alexa import boottime as bot_start_time
from Alexa import db, random_assistant
from Alexa.Core.PyTgCalls import Alexa
from Alexa.Database import (add_nonadmin_chat, add_served_chat,
                            blacklisted_chats, get_assistant, get_authuser,
                            get_authuser_names, get_start, is_nonadmin_chat,
                            is_served_chat, remove_active_chat,
                            remove_nonadmin_chat, save_assistant, save_start)
from Alexa.Decorators.admins import ActualAdminCB
from Alexa.Inline import (custommarkup, dashmarkup, setting_markup,
                          setting_markup2, start_pannel, usermarkup, volmarkup)
from Alexa.Utilities.assistant import get_assistant_details
from Alexa.Utilities.ping import get_readable_time



