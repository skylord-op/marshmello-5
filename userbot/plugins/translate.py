""" Google Translate
Available Commands:
.trt LanguageCode as reply to a message
.trt LangaugeCode | text to translate"""

import emoji
from googletrans import Translator

from userbot.utils import *
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="trt ?(.*)"))
@bot.on(sudo_cmd(pattern="trt ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/skylord_help_chat
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await edit_or_reply(
            event,
            f"`.trt LanguageCode` as reply to a message.\nLanguage codes can be found [here](https://telegra.ph/%F0%9D%95%B1-%F0%9D%95%BE-%F0%9D%95%B1--H%C3%A8ll%E1%BA%9E%C3%B8y-%F0%90%8C%B7%F0%90%8C%B4%E0%A0%8B%E0%A0%8B%F0%90%8C%B1%F0%90%8D%88%F0%90%8C%B8-%F0%90%8C%BE%F0%90%8C%B0%F0%90%8D%80%F0%90%8C%BE-B%E3%83%A0JRANGD%E3%83%A0L-12-04)",
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated**\nFrom {} to {}
{}""".format(
            translated.src, lan, after_tr_text
        )
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_or_reply(event, str(exc))
