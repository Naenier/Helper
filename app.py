from threading import Thread

import time
import schedule

from handlers import app
from telegram_config import tg_id
from messages import msg


def gm_message():
    app.send_message(tg_id.chat_id, msg.good_morning)


def RnP():
    app.send_message(tg_id.chat_id, msg.notification_rnp)


def mentoring_trafik_expert_1():
    app.send_message(tg_id.trafik_expert, msg.notification_two_hour)


def mentoring_trafik_expert_2():
    app.send_message(tg_id.trafik_expert, msg.notification_one_hour)


def mentoring_Rukishaaa_1():
    app.send_message(tg_id.Rukishaaa, msg.notification_two_hour)


def mentoring_Rukishaaa_2():
    app.send_message(tg_id.Rukishaaa, msg.notification_one_hour)


def mentoring_krylova_gv_1():
    app.send_message(tg_id.krylova_gv, msg.notification_two_hour)


def mentoring_krylova_gv_2():
    app.send_message(tg_id.krylova_gv, msg.notification_one_hour)


def mentoring_signora_olga_1():
    app.send_message(tg_id.signora_olga, msg.notification_two_hour)


def mentoring_signora_olga_2():
    app.send_message(tg_id.signora_olga, msg.notification_one_hour)


def mentoring_Malinovskaya_AM_1():
    app.send_message(tg_id.Malinovskaya_AM, msg.notification_two_hour)


def mentoring_Malinovskaya_AM_2():
    app.send_message(tg_id.Malinovskaya_AM, msg.notification_one_hour)


def mentoring_gavrilova_v_smm_1():
    app.send_message(tg_id.gavrilova_v_smm, msg.notification_two_hour)


def mentoring_gavrilova_v_smm_2():
    app.send_message(tg_id.gavrilova_v_smm, msg.notification_one_hour)


def run():
    schedule.every().day.at("08:00").do(gm_message)
    schedule.every().monday.at("09:00").do(RnP)
    schedule.every().saturday.at("08:30").do(mentoring_trafik_expert_1)
    schedule.every().thursday.at("11:30").do(mentoring_trafik_expert_2)
    schedule.every().monday.at("13:30").do(mentoring_Rukishaaa_2)
    schedule.every().thursday.at("09:30").do(mentoring_Rukishaaa_1)
    schedule.every().tuesday.at("13:00").do(mentoring_krylova_gv_2)
    schedule.every().sunday.at("09:30").do(mentoring_krylova_gv_1)
    schedule.every().monday.at("11:30").do(mentoring_signora_olga_2)
    schedule.every().thursday.at("13:30").do(mentoring_signora_olga_1)
    schedule.every().monday.at("10:30").do(mentoring_Malinovskaya_AM_2)
    schedule.every().saturday.at("13:30").do(mentoring_Malinovskaya_AM_1)
    schedule.every().tuesday.at("08:30").do(mentoring_gavrilova_v_smm_2)
    schedule.every().friday.at("08:30").do(mentoring_gavrilova_v_smm_1)

    while True:
        schedule.run_pending()
        time.sleep(1)


Thread(target=run).start()
app.run()
