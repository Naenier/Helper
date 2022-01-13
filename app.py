from threading import Thread

import time
import schedule

from handlers import app
from scheduler_tg import sch_msg


def run():
    # Акселератор
    schedule.every().day.at("08:00").do(sch_msg.gm_message)
    schedule.every().monday.at("09:00").do(sch_msg.RnP)

    # Mentoring X
    schedule.every().saturday.at("08:30").do(sch_msg.mentoring_trafik_expert_1)
    schedule.every().thursday.at("11:30").do(sch_msg.mentoring_trafik_expert_2)
    schedule.every().monday.at("13:30").do(sch_msg.mentoring_Rukishaaa_2)
    schedule.every().thursday.at("09:30").do(sch_msg.mentoring_Rukishaaa_1)
    schedule.every().tuesday.at("13:00").do(sch_msg.mentoring_krylova_gv_2)
    schedule.every().sunday.at("09:30").do(sch_msg.mentoring_krylova_gv_1)
    schedule.every().monday.at("11:30").do(sch_msg.mentoring_signora_olga_2)
    schedule.every().thursday.at("13:30").do(sch_msg.mentoring_signora_olga_1)
    schedule.every().monday.at("10:30").do(sch_msg.mentoring_Malinovskaya_AM_2)
    schedule.every().saturday.at("13:30").do(sch_msg.mentoring_Malinovskaya_AM_1)
    schedule.every().tuesday.at("08:30").do(sch_msg.mentoring_gavrilova_v_smm_2)
    schedule.every().friday.at("08:30").do(sch_msg.mentoring_gavrilova_v_smm_1)

    while True:
        schedule.run_pending()
        time.sleep(1)


Thread(target=run).start()
app.run()
