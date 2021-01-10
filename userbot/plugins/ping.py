from datetime import datetime

from userbot import CMD_HELP, Lastupdate, time
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(admin_cmd(pattern="ping", outgoing=True))
@borg.on(sudo_cmd(pattern="ping", allow_sudo=True))
async def _(event):
    sppidy = await edit_or_reply(event, "`📊 Calculating my ping 🔍`")
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await sppidy.edit(f"**✅ My current ping👇**\n\n ➲ `{ms}` \n ➲ `{uptime}`")


@borg.on(admin_cmd(pattern="pong", outgoing=True))
@borg.on(sudo_cmd(pattern="pong", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000 * 2
    await edit_or_reply(event, f"My current Ping 🎾 {ms} 🤍")


CMD_HELP.update(
    {
        "ping": "**Plugin : **`Ping Pong`\
        \n\n **Syntax : **`.ping`\
        \n**Function : **Shows you the ping speed of server\
        \n\n**Syntax : **`.pong`\
        \n**Function : **Shows you the ping speed of server (Opposite Of Ping)\
        "
    }
)
