import telepot

def enviar_msg(mensagem):
  bot = telepot.Bot('931137616:AAEm2cH0EXEkbcqWYBrFPzPsfqRx2dRCwCY')
  chat = '914925454'
  bot.sendMessage(chat, mensagem)