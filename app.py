from threading import Thread

import time
import schedule

from handlers import app
from scheduler_tg import sch_msg


def run():
    # Акселератор
    scheduler1 = schedule.Scheduler()
    scheduler1.every().monday.at("09:00").do(sch_msg.RnP)
    scheduler1.every().saturday.at("05:03").do(sch_msg.Test)

    # Рассылка Telegram
    scheduler2 = schedule.Scheduler()
    scheduler2.every().friday.at("13:35").do(sch_msg.chats_message_1)
    scheduler2.every(64).minutes.do(sch_msg.chats_message_2)
    scheduler2.every(66).minutes.do(sch_msg.chats_message_3)
    scheduler2.every(62).minutes.do(sch_msg.chats_message_4)
    scheduler2.every(68).minutes.do(sch_msg.chats_message_5)
    scheduler2.every(70).minutes.do(sch_msg.chats_message_6)
    scheduler2.every().friday.at("13:30").do(sch_msg.chats_message_7)
    scheduler2.every(60).minutes.do(sch_msg.chats_message_8)

    while True:
        scheduler1.run_pending()
        scheduler2.run_pending()
        time.sleep(1)


Thread(target=run).start()
app.run()
