from telebotpy.telebot import TelegramBot

#"-1001987318036" #Test Notification
# Replace 'YOUR_TOKEN' and 'YOUR_CHAT_ID' with your actual values
bot = TelegramBot(token="6494364807:AAGTNVySVtdka-pZNkDtv2EegmRyMSt3Qto", chat_id="-1001987318036")
bot.send_text_message("This is a test message.")
# bot.send_document('sampleDoc.txt', "This is a document caption.")
# bot.send_image('car.png', "Image caption.")
