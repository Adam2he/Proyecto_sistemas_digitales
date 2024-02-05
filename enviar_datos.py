import os
import telebot

TELEGRAM_TOKEN="6370513758:AAEI0GT8l5hKiNdP9DYSiJ24OUFzLDKiC58"
CHAT_ID="1426202243"
bot=telebot.TeleBot(TELEGRAM_TOKEN)

def envia_datos():
    archivo=open("/home/pi/ovpns/datos.ovpn","r")
    bot.send_message(CHAT_ID,"Sus datos de VPN. La contraseña es: datos")
    bot.send_document(CHAT_ID,archivo)




