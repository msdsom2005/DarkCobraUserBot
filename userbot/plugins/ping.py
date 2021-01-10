import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"


@borg.on(admin_cmd(pattern=f"ping$", outgoing=True))
@borg.on(sudo_cmd(pattern=f"ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    animation_interval = 0.2
    animation_ttl = range(0, 26)
    await edit_or_reply(event, "ping....")
    animation_chars = ["My 🇵 🇮 🇳 🇬  Is : Calculating...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 26])
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n ➲ `{ms}` \n ➲ `{uptime}`,My 🇵 🇮 🇳 🇬  Is : {} ms".format(
            ms
        )
    )


@borg.on(admin_cmd(pattern="king$"))
@borg.on(sudo_cmd(pattern="king$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    ghanta = borg.uid
    event = await edit_or_reply(event, "__**(★ Kong!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**✦҈͜͡➳ Kong!__**\n★ {ms}\n★ __**My**__ __**Master**__ [{DEFAULTUSER}](tg://user?id={ghanta})"
    )


CMD_HELP.update(
    {
        "ping": "__**PLUGIN NAME :** King__\
    \n\n📌** CMD ★** `.ping`\
    \n**USAGE   ★  **A kind of ping with extra animation\
    \n\n📌** CMD ★** `.king`\
    \n**USAGE   ★  **Shows you the ping speed of server"
    }
)
