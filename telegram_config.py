from dataclasses import dataclass


# Telegram ID
@dataclass(frozen=True)
class Telegram_ID:
	chat_id: str = -1001631451746  # Акселератор
	chat_id_content: str = -1001791209527  # Контент
	sale_mentor: str = '1775652016'  # Личный аккаунт
	files: str = -1001778163472  # Файловая система

	chat_1: str = -1001156193082  # Мари про вакансии - инфобизнес \неделя\
	chat_2: str = -1001273124836  # ВАКАНСИИ И РЕЗЮМЕ В СФЕРЕ ИНФОБИЗНЕС ФРИЛАНС УДАЛЁННАЯ РАБОТА
	chat_3: str = -1001263355588  # РАБОТА DIGITAL ЧАТ
	chat_4: str = -1001586660313  # LUBSITE CLUB (вакансии + поиск работы)
	chat_5: str = -1001402257163  # ФРИЛАНС | УДАЛЕННАЯ РАБОТА ЧАТ
	chat_6: str = -1001514920647  # Вакансии. Работа. Чат.
	chat_7: str = -1001465321166  # EdMarket Club (вакансии) \неделя\
	chat_8: str = -1001313032628  # WORK ON | HR | ФРИЛАНС ЧАТ
	chat_9: str = -1001337059888  # ПОМОГАТОР БЕЗЛИМИТ
	chat_10: str = -1001163797425  # WORK ON | LEADS | ФРИЛАНС ЧАТ
	chat_11: str = -1001460940481  # WORK ON | ФРИЛАНС ЧАТ
	chat_12: str = -1001360151362  # JOBOSPHERE | ФРИЛАНС-ЧАТ
	chat_13: str = -1001375624726  # ФРИЛАНС! УДАЛЁНКА.SlavynskiiMir
	chat_14: str = -1001209503065  # Ищу / Помогу | Фриланс - ЧАТ
	chat_15: str = -1001318197938  # ПОМОГАТОР - БИРЖА ФРИЛАНСА | ВАКАНСИИ | ПОРТФОЛИО | РЕЗЮМЕ
	chat_16: str = -1001425875581  # Помогатор Фрилансеры


tg_id = Telegram_ID()
