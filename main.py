# -*- coding: utf-8 -*-
import telepot
import time
from pprint import pprint
import json
import os

TOKEN = '131072279:AAGJBvp_7LnYq3OfeDAY8LflPIdsQk0NATM'
updateId = 0

bot = telepot.Bot(TOKEN)
bot2 = telepot.DelegatorBot(TOKEN)
print(bot2.getMe())
# me = bot.getMe()
#print(me)


while True:
    response = bot.getUpdates(updateId)
    pprint(response)
#    json_obj = json.load(response)
    for i in response:
        pprint(i['message'])
        chatId = i['message']['chat']['id']
        userId = i['message']['from']['id']
        text = i['message']['text']
        pprint(i['message']['text'])

        show_keyboard = {'keyboard': [['1. 서울로 간다.'], ['2. 부산으로 간다.'],['3. 인천으로 간다.']]}
        bot.sendMessage(chatId, "선택하세요.", reply_markup=show_keyboard)
#        bot.sendMessage(chatId, text)
#        bot.sendMessage(56432486, text)
#        if text == 'reboot':
#            os.system('reboot')

        updateId = i['update_id'] + 1
    time.sleep(0.5)
