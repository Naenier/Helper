from dataclasses import dataclass


# Telegram ID
@dataclass(frozen=True)
class Telegram_ID:
	chat_id: str = '-1001631451746'
	sale_mentor: str = '1775652016'

	trafik_expert: str = '816994285'  # Татьяна Геньсьор
	krylova_gv: str = '302507861'  # Евгения Крылова
	signora_olga: str = '1180786878'  # Ольга Сигнора
	Malinovskaya_AM: str = '1813142601'  # Анна Малиновская
	Rukishaaa: str = '458814686'  # Рукият Дибирова
	gavrilova_v_smm: str = '1341248686'  # Ксения Гаврилова

	notion: str = 'BAACAgIAAxkBAAECJmJh3O4Zu2JE6DMsW7gaPehSZIRS_gACsBQAAn99YUld-a9zUnEyTR4E'  # МК по Notion
	instagram: str = 'BAACAgIAAxkBAAECJmRh3O_b5eYEwvjKQOPlflKL0J7XFwAC6xYAAk2AkUtgLulrBsiBoh4E'  # Check-Up Instagram Like-Centre
	funnel: str = 'BQACAgIAAxkBAAECJmxh3PP9NnegkSx3ftLxuHgm66WF-QACchMAAg0LKUkWNqRb0gWjLh4E'  # Гайд по построению воронки продаж
	woman: str = 'BAACAgIAAxkBAAECJm5h3PUhXAIOIZ56454qxeHgr9yeuwAC1hAAAtK4sEvpb1QeIWGiIB4E'  # Гайд по женской психике
	gift: str = 'BQACAgIAAxkBAAECJnBh3PV4wAc0l35WoxyHaIXQbmeYpQACoBUAAhbW8UvYbO3wOAvNBh4E'  # Гайд по подарку по чертам лица
	armor: str = 'BAACAgIAAxkBAAECJv5h3R0vZrGdMXC4V0rBTrqcMRJucwACwgwAAhxtkEu_pzXIZTRxSx4E'  # Шлюхоброня 2.0
	telemetry: str = 'BQACAgIAAxkBAAECKMth3pXTWcEnof1IXOF15FP_rld_ywACLxIAAl6B-UqnlRCrTCe3Hh4E'  # Программа для спектрального анализа


tg_id = Telegram_ID()
