# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


import os
import re
import subprocess
import sys
import traceback
from html import escape
from inspect import getfullargspec
from io import StringIO
from time import time

from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            Message, ReplyKeyboardMarkup)

from Alexa import SUDOERS, app
from Alexa.Utilities.tasks import add_task, rm_task

# Eval and Sh module from WBB

__MODULE__ = "🪂 ʙʀᴏᴀᴅᴄᴀsᴛ"
__HELP__ = """
**ɴᴏᴛᴇ:**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.


`/broadcast` [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
- ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.


`/broadcast_pin` [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
- ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴡɪᴛʜ ᴍᴇssᴀɢᴇ ɢᴇᴛᴛɪɴɢ ᴘɪɴɴᴇᴅ ɪɴ ᴄʜᴀᴛ [ᴅɪsᴀʙʟᴇᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴs].


`/broadcast_pin_loud` [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
- ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴡɪᴛʜ ᴍᴇssᴀɢᴇ ɢᴇᴛᴛɪɴɢ ᴘɪɴɴᴇᴅ ɪɴ ᴄʜᴀᴛ [ᴇɴᴀʙʟᴇᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴs].

- ᴘᴏᴡᴇʀᴅ ʙʏ 😍 ʀᴏᴄᴋs ᴀɴᴅ @ruhsuzbeyyy
"""


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@app.on_message(
    filters.user(SUDOERS)
    & ~filters.forwarded
    & ~filters.via_bot
    & filters.command("eval")
)
async def executor(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**ɴɪɢɢᴀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴇxᴇᴄᴜᴛᴇ...** 🥺"
        )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    t1 = time()
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"**OUTPUT**:\n```{evaluation.strip()}```"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳", callback_data=f"runtime {t2-t1} Seconds"
                    )
                ]
            ]
        )
        await message.reply_document(
            document=filename,
            caption=f"**ɪɴᴘᴜᴛ:**\n`{cmd[0:980]}`\n\n**ᴏᴜᴛᴘᴜᴛ:**\n`ᴀᴛᴛᴀᴄʜᴇᴅ ᴅᴏᴄᴜᴍᴇɴᴛ`",
            quote=False,
            reply_markup=keyboard,
        )
        await message.delete()
        os.remove(filename)
    else:
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"runtime {round(t2-t1, 3)} Seconds",
                    ),
                    InlineKeyboardButton(
                        text="🗑",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await edit_or_reply(message, text=final_output, reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"runtime"))
async def runtime_func_cq(_, cq):
    runtime = cq.data.split(None, 1)[1]
    await cq.answer(runtime, show_alert=True)


@app.on_message(
    filters.user(SUDOERS)
    & ~filters.forwarded
    & ~filters.via_bot
    & filters.command("sh"),
)
async def shellrunner(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="**ᴜsᴀɢᴇ:**\n/sh ɢɪᴛ ᴘᴜʟʟ")
    text = message.text.split(None, 1)[1]
    if "\n" in text:
        code = text.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except Exception as err:
                print(err)
                await edit_or_reply(message, text=f"**ERROR:**\n```{err}```")
            output += f"**{code}**\n"
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", text)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as err:
            print(err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            return await edit_or_reply(
                message, text=f"**ERROR:**\n```{''.join(errors)}```"
            )
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await app.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.message_id,
                caption="`Output`",
            )
            return os.remove("output.txt")
        await edit_or_reply(message, text=f"**OUTPUT:**\n```{output}```")
    else:
        await edit_or_reply(message, text="**OUTPUT: **\n`No output`")
