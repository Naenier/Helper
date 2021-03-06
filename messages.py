from dataclasses import dataclass


# Messages
@dataclass(frozen=True)
class Messages:
	notification_rnp: str = '**Напоминаю, что через час начинается РнП.**\n' \
	                        'Приготовьте блокноты/ ручки и нажмите на таймер, чтобы включить уведомление.'
	self_presentation_hash: str = '#помогу #продажи #маркетинг\n' \
	                              '\n' \
	                              '💡Илья, наставник по продажам и маркетингу в сфере инфобизнеса.\n' \
	                              '\n' \
	                              'Ко мне можно обратиться по вопросам:\n' \
	                              '• нет продаж, мало продаж\n' \
	                              '• тяжело, некомфортно, неприятно продавать свой продукт/ услугу\n' \
	                              '• запуски курса/ наставничества/ марафона/ интенсива\n' \
	                              '• проведение онлайн-мероприятий (вебинары, мастер-классы)\n' \
	                              '\n' \
	                              'Обучаю мягким продажам с самой высокой конверсией. А мои ученики продают с наслаждением. ' \
	                              'Гарантия увеличения конверсии в продажу в 3 раза за 15 минут консультации или возвращаю деньги.\n' \
	                              '▪️Создам для тебя персональную технику продаж, учитывая твои особенности психики\n' \
	                              '▪️Клиенты сами захотят у тебя купить всё, что ты им предложишь\n' \
	                              '▪️Секретные технологии в понимании психологии клиента\n' \
	                              '\n' \
	                              'Приглашаю на двухчасовой индивидуальный разбор проекта, где ты получишь пошаговый план запуска твоего продукта. ' \
	                              'У тебя захотят купить всё, что предложишь.\n' \
	                              '\n' \
	                              'Зачем?\n' \
	                              '- готовая стратегия выхода проекта на новый уровень\n' \
	                              '- ключевые тактические действия "ручками" здесь и сейчас, необходимые для результата\n' \
	                              '\n' \
	                              'Формат видео-созвона в течение 2х часов под запись, которую скину после стратсессии.\n' \
	                              '\n' \
	                              '1. Анализируем проект/продукт\n' \
	                              '2. Обозначаем цель (результат)\n' \
	                              '3. Выстраиваем стратегию с пошаговым планом\n' \
	                              '4. Ставим тактические задачи, необходимые для результата\n' \
	                              '5. Обсуждаем недостающие компетенции при необходимости\n' \
	                              '\n' \
	                              'Чтобы записаться, напиши в личку "Стратсессия"\n'
	self_presentation_url_hash: str = '#помогу #продажи #маркетинг\n' \
	                                  '\n' \
	                                  '💡Илья, наставник по продажам и маркетингу в сфере инфобизнеса.\n' \
	                                  '\n' \
	                                  'Ко мне можно обратиться по вопросам:\n' \
	                                  '• нет продаж, мало продаж\n' \
	                                  '• тяжело, некомфортно, неприятно продавать свой продукт/ услугу\n' \
	                                  '• запуски курса/ наставничества/ марафона/ интенсива\n' \
	                                  '• проведение онлайн-мероприятий (вебинары, мастер-классы)\n' \
	                                  '\n' \
	                                  'Обучаю мягким продажам с самой высокой конверсией. А мои ученики продают с наслаждением. ' \
	                                  'Гарантия увеличения конверсии в продажу в 3 раза за 15 минут консультации или возвращаю деньги.\n' \
	                                  '\n' \
	                                  '▪️Создам для тебя персональную технику продаж, учитывая твои особенности психики\n' \
	                                  '▪️Клиенты сами захотят у тебя купить всё, что ты им предложишь\n' \
	                                  '▪️Секретные технологии в понимании психологии клиента\n' \
	                                  '\n' \
	                                  'Приглашаю на двухчасовой индивидуальный разбор проекта, где ты получишь пошаговый план запуска твоего продукта. ' \
	                                  'У тебя захотят купить всё, что предложишь.\n' \
	                                  '\n' \
	                                  'Зачем?\n' \
	                                  '- готовая стратегия выхода проекта на новый уровень\n' \
	                                  '- ключевые тактические действия "ручками" здесь и сейчас, необходимые для результата\n' \
	                                  '\n' \
	                                  'Формат видео-созвона в течение 2х часов под запись, которую скину после стратсессии.\n' \
	                                  '\n' \
	                                  '1. Анализируем проект/продукт\n' \
	                                  '2. Обозначаем цель (результат)\n' \
	                                  '3. Выстраиваем стратегию с пошаговым планом\n' \
	                                  '4. Ставим тактические задачи, необходимые для результата\n' \
	                                  '5. Обсуждаем недостающие компетенции при необходимости\n' \
	                                  '\n' \
	                                  'Чтобы записаться, жми — <a href="https://vk.com/soulssaler?w=product-211087266_5248134%2Fquery">Стратсессия</a>\n'
	self_presentation: str = '💡Илья, наставник по продажам и маркетингу в сфере инфобизнеса.\n' \
	                         '\n' \
	                         'Ко мне можно обратиться по вопросам:\n' \
	                         '• нет продаж, мало продаж\n' \
	                         '• тяжело, некомфортно, неприятно продавать свой продукт/ услугу\n' \
	                         '• запуски курса/ наставничества/ марафона/ интенсива\n' \
	                         '• проведение онлайн-мероприятий (вебинары, мастер-классы)\n' \
	                         '\n' \
	                         'Обучаю мягким продажам с самой высокой конверсией. А мои ученики продают с наслаждением. ' \
	                         'Гарантия увеличения конверсии в продажу в 3 раза за 15 минут консультации или возвращаю деньги.\n' \
	                         '\n' \
	                         '▪️Создам для тебя персональную технику продаж, учитывая твои особенности психики\n' \
	                         '▪️Клиенты сами захотят у тебя купить всё, что ты им предложишь\n' \
	                         '▪️Секретные технологии в понимании психологии клиента\n' \
	                         '\n' \
	                         'Приглашаю на двухчасовой индивидуальный разбор проекта, где ты получишь пошаговый план запуска твоего продукта. ' \
	                         'У тебя захотят купить всё, что предложишь.\n' \
	                         '\n' \
	                         'Зачем?\n' \
	                         '- готовая стратегия выхода проекта на новый уровень\n' \
	                         '- ключевые тактические действия "ручками" здесь и сейчас, необходимые для результата\n' \
	                         '\n' \
	                         'Формат видео-созвона в течение 2х часов под запись, которую скину после стратсессии.\n' \
	                         '\n' \
	                         '1. Анализируем проект/продукт\n' \
	                         '2. Обозначаем цель (результат)\n' \
	                         '3. Выстраиваем стратегию с пошаговым планом\n' \
	                         '4. Ставим тактические задачи, необходимые для результата\n' \
	                         '5. Обсуждаем недостающие компетенции при необходимости\n' \
	                         '\n' \
	                         'Чтобы записаться, жми — <a href="https://vk.com/soulssaler?w=product-211087266_5248134%2Fquery">Стратсессия</a>\n'
	contacts: str = '**Контакты:**\n' \
	                '<a href="tg://user?id=869367908">Telegram</a>\n' \
	                '<a href="https://www.instagram.com/ilya.mentor/">Instagram</a>\n' \
	                '\n' \
	                '**Реквизиты:**\n' \
	                '**Карта Tinkoff:** 5536 9139 0486 3012\n' \
	                '**Карта Сбербанк:** 4279 3806 2065 9229\n' \
	                '\n' \
	                '__Система быстрых платежей__\n' \
	                '+79996463455\n' \
	                '\n' \
	                'ILYA KISELEV'
	help: str = 'Вот список доступных запрограммированных команд:\n' \
	            '**`.self`** — Обо мне\n' \
	            '**`.contacts`** — Контакты и реквизиты\n' \
	            '**`.accelerator`** — Комьюнити экспертов — Акселератор\n' \
	            '**`.services`** — Перечень доступных услуг\n' \
	            '**`.telemetry`** — Участвовать в исследовании\n' \
	            '\n' \
	            'Можешь просто скопировать мне одну из нужных команд.\n' \
	            'Нажми на команду, и она автоматически скопируется. Вставь её обратно в чат и отправь.'
	accelerator: str = '<a href="https://t.me/+HWsIjcb758lmMmIy">Акселератор</a> ← кликабельная ссылка'
	services: str = '**Перечень доступных услуг:**\n' \
	                '\n' \
	                '**1. Наставничество по продажам** — двухмесячное индивидуальное сопровождение проекта с ' \
	                'обучением навыку продаж и другим навыкам взаимодействия с клиентами;\n' \
	                '\n' \
	                '**2. Консультация по нейротипологии** — индивидуальный двухчасовой разбор твоих особенностей психики, ' \
	                'сильных и слабых сторон и предрасположенностей;\n' \
	                '\n' \
	                '**3. Личная консультация по запросу** — двухчасовая сессия с решением поставленной задачи;\n' \
	                '\n' \
	                '**4. Аудит продаж** — анализ навыка продаж с получением индивидуальных рекомендаций для увеличения ' \
	                'конверсии в продажу минимум +30%;\n' \
	                '\n' \
	                '**5. Аудит проекта командой из 3-х менторов** — бесплатный индивидуальный разбор проекта командой из трёх менторов ' \
	                'с получением стратегии развития проекта за 1 час.\n' \
	                'Просто отправь мне цифру, и я расскажу об интересующей тебя услуги.'
	telemetry: str = '**Для проведения спектрального анализа тебе понадобится ноутбук или компьютер с веб-камерой.**\n' \
	                 '\n' \
	                 'Телеметрия займёт у тебя ровно 5 минут времени. Далее мне понадобится некоторое время на анализ.\n' \
	                 '\n' \
	                 'Сначала установи себе программу, которая будет считывать и записывать твои показатели. После чего напиши мне.\n' \
	                 '\n' \
	                 'Если возникнут вопросы, напиши мне, я поясню.'
	instruction: str = 'https://drive.google.com/file/d/1l6RQZ0a_3reccpoBg0qfA77j8Kv--06m/view?usp=sharing'


msg = Messages()
