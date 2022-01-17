from dataclasses import dataclass


# Telegram ID
@dataclass(frozen=True)
class Telegram_ID:
	chat_id: str = -1001631451746  # Акселератор
	x10: str = -1001695701278  # X10
	sale_mentor: str = '1775652016'  # Личный аккаунт
	files: str = -1001778163472  # Файловая система

	chat_1: str = -1001156193082  # Мари про вакансии - инфобизнес \неделя\
	chat_2: str = -1001557281043  # WorkLance-3
	chat_3: str = -1001263355588  # РАБОТА DIGITAL ЧАТ
	chat_4: str = -1001586660313  # LUBSITE CLUB (вакансии + поиск работы)
	chat_5: str = -1001402257163  # ФРИЛАНС | УДАЛЕННАЯ РАБОТА ЧАТ
	chat_6: str = -1001514920647  # Вакансии. Работа. Чат.
	chat_7: str = -1001465321166  # EdMarket Club (вакансии) \неделя\
	chat_8: str = -1001313032628  # WORK ON | HR | ФРИЛАНС ЧАТ

	trafik_expert: str = '816994285'  # Татьяна
	krylova_gv: str = '302507861'  # Евгения Крылова
	signora_olga: str = '1180786878'  # Ольга Сигнора
	Malinovskaya_AM: str = '1813142601'  # Анна Малиновская
	Rukishaaa: str = '458814686'  # Рукият Дибирова
	gavrilova_v_smm: str = '1341248686'  # Ксения Гаврилова


tg_id = Telegram_ID()
