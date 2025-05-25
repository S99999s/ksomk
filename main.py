import requests
import telebot,time
import random
from telebot import types
from Demon import Tele
import os
token ='8120969680:AAFBKpokM4UoTKR5P-r7vkf_haCJAlvNvzc'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '6832492482'
SLEEP_TIME = random.uniform(20,40)
@bot.message_handler(commands=["start"])
def start(message):
  if not str(message.chat.id) == '6832492482':
    bot.reply_to(message, "Only for KoKo Bhone Pyae Thu🙄💗")
    return
  bot.reply_to(message,"Send the file now")
@bot.message_handler(content_types=["document"])
def main(message):
  if not str(message.chat.id) == '6832492482':
    bot.reply_to(message, "Only for KoKo Bhone Pyae Thu🙄💗")
    return
  dd = 0
  live = 0
  ch = 0
  ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
  ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
  with open("combo.txt", "wb") as w:
    w.write(ee)
  try:
    with open("combo.txt", 'r') as file:
      lino = file.readlines()
      total = len(lino)
      for cc in lino:
        current_dir = os.getcwd()
        for filename in os.listdir(current_dir):
          if filename.endswith(".stop"):
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @xosold')
            os.remove('stop.stop')
            return
        try:
          data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()

        except:
          pass
        try:
          bank=(data['bank']['name'])
        except:
          bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
        try:
          emj=(data['country']['emoji'])
        except:
          emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
        try:
          cn=(data['country']['name'])
        except:
          cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
        try:
          dicr=(data['scheme'])
        except:
          dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
        try:
          typ=(data['type'])
        except:
          typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
        try:
          url=(data['bank']['url'])
        except:
          url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')


        try:
          last = str(Tele(cc))
        except Exception as e:
          print(e)
          last = "ERROR"
        if 'risk' in last:
          last='declined'
        elif 'Duplicate' in last:
          last='Approved'
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
        status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u8')
        cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
        cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
        cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
        stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
        mes.add(cm1,status, cm3, cm4, cm5, stop)
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @xosold ''', reply_markup=mes)
        msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 🔥
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘾𝙑𝙑 𝘾𝙃𝘼𝙍𝙂𝙀𝘿 5$ 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @xosold
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
        print(last)
        if 'success' in last or 'cardBrand' in last or 'Thank you for your message.' in last or 'subscriberId' in last :
          live += 1
          bot.reply_to(message, msg)
        elif 'security code is incorrect' in last or 'security code is invalid' in last:
          msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘾𝘾𝙉 𝙇𝙄𝙑𝙀
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @xosold
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
          live += 1
          bot.reply_to(message, msg)
        elif 'True' in last:
          msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝙄𝙊𝙒 𝙁𝙐𝙉𝘿𝙎
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @xosold
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
          live += 1
          bot.reply_to(message, msg)
        else:
          dd += 1
          time.sleep(SLEEP_TIME)
  except Exception as e:
    print(e)
  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @xosold')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
  with open("stop.stop", "w") as file:
    pass
print("Bot is running...")
bot.polling()