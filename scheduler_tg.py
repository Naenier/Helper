from dataclasses import dataclass
from telegram_config import tg_id
from messages import msg
from handlers import app


# Messages
@dataclass(frozen=True)
class Schedule_Message:
	@staticmethod
	def gm_message():
		app.send_message(tg_id.chat_id, msg.good_morning)

	@staticmethod
	def RnP():
		app.send_message(tg_id.chat_id, msg.notification_rnp)

	@staticmethod
	def mentoring_trafik_expert_1():
		app.send_message(tg_id.trafik_expert, msg.notification_two_hour)

	@staticmethod
	def mentoring_trafik_expert_2():
		app.send_message(tg_id.trafik_expert, msg.notification_one_hour)

	@staticmethod
	def mentoring_Rukishaaa_1():
		app.send_message(tg_id.Rukishaaa, msg.notification_two_hour)

	@staticmethod
	def mentoring_Rukishaaa_2():
		app.send_message(tg_id.Rukishaaa, msg.notification_one_hour)

	@staticmethod
	def mentoring_krylova_gv_1():
		app.send_message(tg_id.krylova_gv, msg.notification_two_hour)

	@staticmethod
	def mentoring_krylova_gv_2():
		app.send_message(tg_id.krylova_gv, msg.notification_one_hour)

	@staticmethod
	def mentoring_signora_olga_1():
		app.send_message(tg_id.signora_olga, msg.notification_two_hour)

	@staticmethod
	def mentoring_signora_olga_2():
		app.send_message(tg_id.signora_olga, msg.notification_one_hour)

	@staticmethod
	def mentoring_Malinovskaya_AM_1():
		app.send_message(tg_id.Malinovskaya_AM, msg.notification_two_hour)

	@staticmethod
	def mentoring_Malinovskaya_AM_2():
		app.send_message(tg_id.Malinovskaya_AM, msg.notification_one_hour)

	@staticmethod
	def mentoring_gavrilova_v_smm_1():
		app.send_message(tg_id.gavrilova_v_smm, msg.notification_two_hour)

	@staticmethod
	def mentoring_gavrilova_v_smm_2():
		app.send_message(tg_id.gavrilova_v_smm, msg.notification_one_hour)


sch_msg = Schedule_Message()