"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @Cracker30
import asyncio
import time
from userbot.plugins.timefunc import uptimebot, get_readable_time
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

uptime = get_readable_time((time.time() - uptimebot))
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
currentversion = "3.0"

if issudousing:
    amiusingsudo = 'Active ✅'
else:
    amiusingsudo = 'Inactive ❌'

if islogokay:
    logchat = 'Connected ✅'
else:
    logchat = 'Dis-Connected ❌'

@Cracker30😈
PM_IMG = ''https://telegra.ph/file/940a3c870af4cf44dc5c0.jpg
pm_caption = "➥ DARKHACKER😈🔥 ONLINE\n\n"
pm_caption += "➥ ☆SYSTEMS S.T.A.T.S☆\n"😈
pm_caption += "➥ ☆T.E.L.E.T.H.O.NVersion: 1.15.0 \n"😈
pm_caption += "➥ ☆P.Y.T.H.O.N☆: 3.7.4 \n"😈
pm_caption += f"➥ ☆Uptime☆ : {uptime} \n"
pm_caption += "➥ ☆Database•Status:  Functional\n"😈
pm_caption += "➥ ☆O°S : Slim Buster \n"😈
pm_caption += "➥ ☆Current.Branch : Master\n"😈
pm_caption += f"➥ ☆V.E.R.S.I.O.N : {currentversion}\n"😈
pm_caption += f"➥ ☆S.U.D.O : {amiusingsudo}\n"😈                                                                    
pm_caption += f"➥ ☆Log Connections : {logchat} \n"😈
pm_caption += f"➥ ☆My Boss : {DEFAULTUSER} \n"😈
pm_caption += "➥ DARKHACKER😈
pm_caption += "[DARKHACKER 😈](https://telegra.ph/file/940a3c870af4cf44dc5c0.jpg"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()