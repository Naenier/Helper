from dataclasses import dataclass
from telegram_config import tg_id
from messages import msg
from handlers import app


# Messages
@dataclass(frozen=True)
class Schedule_Message:
	@staticmethod
	def RnP():
		app.send_message(tg_id.chat_id, msg.notification_rnp)

	@staticmethod
	def X10():
		app.send_message(tg_id.chat_id, msg.notification_x10)

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

	@staticmethod
	def chats_message_1():
		app.send_message(tg_id.chat_1, msg.self_presentation_url_hash)

	@staticmethod
	def chats_message_2():
		app.send_message(tg_id.chat_2, msg.self_presentation_hash)

	@staticmethod
	def chats_message_3():
		app.send_message(tg_id.chat_3, msg.self_presentation_hash)

	@staticmethod
	def chats_message_4():
		app.send_message(tg_id.chat_4, msg.self_presentation_hash)

	@staticmethod
	def chats_message_5():
		app.send_message(tg_id.chat_5, msg.self_presentation_hash)

	@staticmethod
	def chats_message_6():
		app.send_message(tg_id.chat_6, msg.self_presentation_hash)

	@staticmethod
	def chats_message_7():
		app.send_message(tg_id.chat_7, msg.self_presentation_hash)

	@staticmethod
	def chats_message_8():
		app.send_message(tg_id.chat_8, msg.self_presentation_hash)


sch_msg = Schedule_Message()