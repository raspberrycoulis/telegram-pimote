#!/usr/bin/env python

import time, datetime
import telepot
import os
from telepot.loop import MessageLoop

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Received: %s' % command
    if command == 'All on':
        telegram_bot.sendMessage (chat_id, str("Turning both on!"))
        os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
    elif command == 'All off':
        telegram_bot.sendMessage (chat_id, str("Turning both off!"))
        os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
    elif command == 'Socket 1 on':
        telegram_bot.sendMessage (chat_id, str("Turning socket 1 on!"))
        os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
    elif command == 'SOcket 1 off':
        telegram_bot.sendMessage (chat_id, str("Turning socket 1 off!"))
        os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
    elif command == 'Socket 2 on':
        telegram_bot.sendMessage (chat_id, str("Turning socket 2 on!"))
        os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
    elif command == 'Socket 2 off':
        telegram_bot.sendMessage (chat_id, str("Turning socket 2 off!"))
        os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')

telegram_bot = telepot.Bot('INSERT-BOT-TOKEN-HERE')
MessageLoop(telegram_bot, action).run_as_thread()

print 'Telegram PiMote Control Up and Running....'
while 1:
    time.sleep(10)
