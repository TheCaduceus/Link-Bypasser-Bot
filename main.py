import telebot
import bypasser
import os
from config import log, Vars
import ddl

# Setup Logger
file_handler = log.FileHandler('runtime-log.txt')
formatter = log.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

# log.warning() - For Missing Values
# log.error() - For Error in Bypass / including if occured due to missing values
# log.info() - Received Links / Bot General Messages

TOKEN = Vars[0]
GDTot_Crypt = Vars[1]
Laravel_Session = Vars[2]
XSRF_TOKEN = Vars[3]
KCRYPT = Vars[4]
DCRYPT = Vars[5]
HCRYPT = Vars[6]
KATCRYPT = Vars[7]

# Bot
bot = telebot.TeleBot(TOKEN)

# start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔗 *Available Sites* \n\n  \
 `/dl` - _direct download link (/ddllist)_ \n  \
 `/af` - _adfly_ \n  \
 `/gp` - _gplinks_ \n  \
 `/dp` - _droplink_ \n  \
 `/lv` - _linkvertise_ \n  \
 `/rl` - _rocklinks_ \n  \
 `/gd` - _gdrive look-alike (/gdlist)_ \n  \
 `/ot` - _others (/otlist)_ \n  \
 `/ou` - _ouo_ \n  \
 `/gt` - _gdtot_ \n  \
 `/sh` - _sharer_ \n  \
 `/ps` - _psa_ \n  \
 `/st` - _shorte_ \n  \
 `/pi` - _pixl_ \n  \
 `/gy` - _gyanilinks_ \n  \
 `/sg` - _shortingly_ \n  \
 `/su` - _shareus_ \n  \
 `/fc` - _filecrypt_ \n  \
 `/ko` - _kolop_ \n  \
 `/df` - _drivefire_ \n  \
 `/hd` - _hubdrive_ \n  \
 `/kd` - _katdrive_ \n\n\
_reply to the link with command or use format /xx link_",
parse_mode="Markdown")


# direct download link
@bot.message_handler(commands=['dl'])
def dl(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/dl ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received DDL Link {url}")
    msg = bot.reply_to(message, "⚡ _generating..._", parse_mode="Markdown")
    link = ddl.direct_link_generator(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# katdrive
@bot.message_handler(commands=['kd'])
def kd(message):
    if KATCRYPT == "":
        bot.reply_to(message, "🚫 _You can't use this because_ *KATDRIVE_CRYPT* _ENV is not set_", parse_mode="Markdown")
        log.info("Unable to bypass KatDrive Link due to absence of Cookie(s).")
        return
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/kd ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received KatDrive Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.katdrive_dl(url, KATCRYPT)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# hubdrive
@bot.message_handler(commands=['hd'])
def hd(message):
    if HCRYPT == "":
        bot.reply_to(message, "🚫 _You can't use this because_ *HUBDRIVE_CRYPT* _ENV is not set_", parse_mode="Markdown")
        log.error("Unable to bypass HubDrive Link due to absence of Cookie(s).")
        return

    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/hd ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received HubDrive Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.hubdrive_dl(url, HCRYPT)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# drivefire
@bot.message_handler(commands=['df'])
def df(message):
    if DCRYPT == "":
        bot.reply_to(message, "🚫 _You can't use this because_ *DRIVEFIRE_CRYPT* _ENV is not set_", parse_mode="Markdown")
        log.error("Unable to bypass DriveFire Link due to absence of Cookie(s).")
        return

    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/df ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received DriveFire Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.drivefire_dl(url, DCRYPT)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# kolop
@bot.message_handler(commands=['ko'])
def ko(message):
    if KCRYPT == "":
        bot.reply_to(message, "🚫 _You can't use this because_ *KOLOP_CRYPT* _ENV is not set_", parse_mode="Markdown")
        log.error("Unable to bypass Kolop Link due to absence of Cookie(s).")
        return

    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/ko ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received kolop Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.kolop_dl(url, KCRYPT)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# filecrypt
@bot.message_handler(commands=['fc'])
def fc(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/fc ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received FileCrypt Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.filecrypt(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# shareus
@bot.message_handler(commands=['su'])
def su(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/su ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received ShareUs Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.shareus(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# shortingly
@bot.message_handler(commands=['sg'])
def sg(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/sg ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Shortingly Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.shortlingly(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# gyanilinks
@bot.message_handler(commands=['gy'])
def gy(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/gy ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Gyanilinks Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.gyanilinks(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# pixl
@bot.message_handler(commands=['pi'])
def pi(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/pi ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Pixl Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.pixl(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# shorte
@bot.message_handler(commands=['st'])
def st(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/st ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Shorte Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.sh_st_bypass(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# psa
@bot.message_handler(commands=['ps'])
def ps(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/ps ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received PSA Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    links = bypasser.psa_bypasser(url)
    bot.edit_message_text(f'_{links}_', msg.chat.id, msg.id, parse_mode="Markdown")


# sharer pw
@bot.message_handler(commands=['sh'])
def sh(message):
    if XSRF_TOKEN == "" or Laravel_Session == "":
        bot.reply_to(message, "🚫 _You can't use this because_ *XSRF_TOKEN* _and_ *Laravel_Session* _ENV are not set_", parse_mode="Markdown")
        log.error("Unable to bypass Sharer.pw Link due to absence of Cookie(s).")
        return

    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/sh ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Sharer.pw Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.sharer_pw(url, Laravel_Session, XSRF_TOKEN)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# gdtot url
@bot.message_handler(commands=['gt'])
def gt(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/gt ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received GdToT Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.gdtot(url,GDTot_Crypt)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# adfly short url
@bot.message_handler(commands=['af'])
def af(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/af ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received AdFly Link: {url})
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    out = bypasser.adfly(url)
    link = out['bypassed_url']
    try:    
        bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")
    except:
        bot.edit_message_text("_Failed to Bypass_", msg.chat.id, msg.id, parse_mode="Markdown")


# gplinks short url
@bot.message_handler(commands=['gp'])
def gp(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/gp ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received GPLinks Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.gplinks(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# droplink url
@bot.message_handler(commands=['dp'])
def dp(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/dp ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received DropLink: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.droplink(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")
   

# linkvertise short url
@bot.message_handler(commands=['lv'])
def lv(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/lv ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Linkvertise Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.linkvertise(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# rocklinks link
@bot.message_handler(commands=['rl'])
def rl(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/rl ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received RockLinks Link: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.rocklinks(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown")


# ouo
@bot.message_handler(commands=['ou'])
def ou(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/ou ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    print("You Have Entered ouo:",url)
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.ouo(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown") 


# gd look a like
@bot.message_handler(commands=['gd'])
def gd(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/gd ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received GD Look-A-Like Link: {url})
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.unified(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown") 


# others
@bot.message_handler(commands=['ot'])
def ot(message):
    try:
        url = message.reply_to_message.text
    except:
        try:
            url = message.text.split("/ot ")[1]
        except:
            bot.reply_to(message, "⚠️ _Invalid format, either_ *reply* _to a_ *link* _or use_ */xx link*", parse_mode="Markdown")
            return
    log.info(f"Received Others links: {url}")
    msg = bot.reply_to(message, "🔎 _bypassing..._", parse_mode="Markdown")
    link = bypasser.others(url)
    bot.edit_message_text(f'_{link}_', msg.chat.id, msg.id, parse_mode="Markdown") 


# gd list
@bot.message_handler(commands=['gdlist'])
def gdlis(message):
    list = """_
- appdrive.in \n\
- driveapp.in \n\
- drivehub.in \n\
- gdflix.pro \n\
- drivesharer.in \n\
- drivebit.in \n\
- drivelinks.in \n\
- driveace.in \n\
- drivepro.in \n\
          _"""
    bot.reply_to(message, list, parse_mode="Markdown")


# others list
@bot.message_handler(commands=['otlist'])
def otlis(message):
    list="""_
- exe.io/exey.io \n\
- sub2unlock.net/sub2unlock.com \n\
- rekonise.com \n\
- letsboost.net \n\
- ph.apps2app.com \n\
- mboost.me	\n\
- sub4unlock.com \n\
- ytsubme.com \n\
- bit.ly \n\
- social-unlock.com	\n\
- boost.ink	\n\
- goo.gl \n\
- shrto.ml \n\
- t.co \n\
- tinyurl.com
    _"""
    bot.reply_to(message, list, parse_mode="Markdown")       


# ddl list
@bot.message_handler(commands=['ddllist'])
def ddllis(message):
    list="""_
- disk.yandex.com \n\
- mediafire.com \n\
- uptobox.com \n\
- osdn.net \n\
- github.com \n\
- hxfile.co \n\
- anonfiles.com \n\
- letsupload.io \n\
- 1drv.ms(onedrive) \n\
- pixeldrain.com \n\
- antfiles.com \n\
- streamtape.com \n\
- bayfiles.com \n\
- racaty.net \n\
- 1fichier.com \n\
- solidfiles.com \n\
- krakenfiles.com \n\
- upload.ee \n\
- mdisk.me \n\
- wetransfer.com \n\
- gofile.io \n\
- dropbox.com \n\
- zippyshare.com \n\
- megaup.net \n\
- fembed.net, fembed.com, femax20.com, fcdn.stream, feurl.com, layarkacaxxi.icu, naniplay.nanime.in, naniplay.nanime.biz, naniplay.com, mm9842.com \n\
- sbembed.com, watchsb.com, streamsb.net, sbplay.org
    _"""
    bot.reply_to(message, list, parse_mode="Markdown")       

# server loop
log.info("--BOT STARTED--")
bot.infinity_polling()
