from dataclasses import dataclass


# Telegram ID
@dataclass(frozen=True)
class Telegram_ID:
	chat_id: str = -1001631451746  # Акселератор
	sale_mentor: str = '1775652016'  # Личный аккаунт
	files: str = -1001778163472  # Файловая система

	chat_1: str = '-1001156193082'  # Мари про вакансии - инфобизнес \неделя\
	chat_2: str = '-1001557281043'  # WorkLance-3
	chat_3: str = '-1001263355588'  # РАБОТА DIGITAL ЧАТ
	chat_4: str = '-1001586660313'  # LUBSITE CLUB (вакансии + поиск работы)
	chat_5: str = '-1001402257163'  # ФРИЛАНС | УДАЛЕННАЯ РАБОТА ЧАТ
	chat_6: str = '-1001514920647'  # Вакансии. Работа. Чат.
	chat_7: str = '-1001465321166'  # EdMarket Club (вакансии) \неделя\
	chat_8: str = '-1001337059888'  # ПОМОГАТОР БЕЗЛИМИТ

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
	telemetry: str = 'BQACAgIAAxkBAAECKaNh3zRnF3x1_gAB2Stgt8eTmnno4sUAAi8SAAJegflKp5UQq0wntx4eBA'  # Программа для спектрального анализа


tg_id = Telegram_ID()
