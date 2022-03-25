from threading import Thread

import time
import schedule

from handlers import app
from scheduler_tg import sch_msg


def run():
    # Акселератор
    schedule.every().monday.at("09:00").do(sch_msg.RnP)

    # Рассылка Telegram
    schedule.every().friday.at("13:30").do(sch_msg.chats_message_1)
    schedule.every(64).minutes.do(sch_msg.chats_message_2)
    schedule.every(66).minutes.do(sch_msg.chats_message_3)
    schedule.every(62).minutes.do(sch_msg.chats_message_4)
    schedule.every(68).minutes.do(sch_msg.chats_message_5)
    schedule.every(70).minutes.do(sch_msg.chats_message_6)
    schedule.every().friday.at("13:30").do(sch_msg.chats_message_7)
    schedule.every(60).minutes.do(sch_msg.chats_message_8)

    while True:
        schedule.run_pending()
        time.sleep(1)


Thread(target=run).start()
app.run()
