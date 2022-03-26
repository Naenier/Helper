from dataclasses import dataclass
from telegram_config import tg_id
from messages import msg
from handlers import app


# Messages
@dataclass(frozen=True)
class Schedule_Message:
	@staticmethod
	def RnP_notify():
		app.send_message(tg_id.chat_id, msg.notification_rnp)

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