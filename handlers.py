from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

from telegram_config import tg_id
from messages import msg
from udb import user_database


app = Client("my_account")
db = user_database('user_database.db')


@app.on_message(filters.command("allusers", prefixes="."))
def help_message(_, message):
    for member in app.iter_chat_members(chat_id=tg_id.chat_id):
        app.send_message("me", member.user.username)
        sleep(0.3)


@app.on_message(filters.regex("Mentoring X") & ~filters.me)
def message_id(_, message):
    if message.chat.type not in "private":
        return
    next_id = message.message_id + 1
    app.send_message(chat_id=message.from_user.id, text='Запрос принят')
    perc = 0

    while perc < 100:
        try:
            text = "Идет сбор данных..." + str(perc) + "%"
            app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text=text)

            perc += random.randint(10, 17)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text="🟢 Завершено")
    sleep(1)

    app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text="🔜 Регистрация...")
    perc = 0

    while perc < 100:
        try:
            text = "🔜 Регистрация..." + str(perc) + "%"
            app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text=text)

            perc += random.randint(1, 5)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    app.edit_message_text(
        chat_id=message.from_user.id,
        message_id=next_id,
        text="🟢 Спасибо. Ты успешно зарегестрирован в системе.\n"
             "**Это автоматическое сообщение бота**",
        parse_mode="markdown")
    app.send_message('me', f'Пользователь зарегестрирован @{message.from_user.username} {message.from_user.id}')


@app.on_message(filters.command("help", prefixes="."))
def help_message(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat,
                     text=msg.help)


@app.on_message(filters.command("services", prefixes="."))
def services(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat,
                     text=msg.services)


@app.on_message(filters.command("accelerator", prefixes="."))
def accelerator(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat,
                     text=msg.accelerator,
                     disable_web_page_preview=True)


@app.on_message(filters.command("instruction", prefixes="."))
def instruction(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat,
                     text=msg.instruction,
                     disable_web_page_preview=True)


@app.on_message(filters.command("self", prefixes="."))
def self(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat,
                     text=msg.self_presentation,
                     disable_web_page_preview=True)


@app.on_message(filters.command("contacts", prefixes="."))
def contacts(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat,
                     text=msg.contacts)


@app.on_message(filters.command("notion", prefixes="."))
def notion(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=16)


@app.on_message(filters.command("instagram", prefixes="."))
def instagram(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=22)


@app.on_message(filters.command("woman", prefixes="."))
def woman(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=20)


@app.on_message(filters.command("armor", prefixes="."))
def armor(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=28)


@app.on_message(filters.command("funnel", prefixes="."))
def funnel(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=18)


@app.on_message(filters.command("secret", prefixes="."))
def secret(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=24)


@app.on_message(filters.command("gift", prefixes="."))
def gift(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=26)


@app.on_message(filters.command("testosterone", prefixes="."))
def testosterone(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.forward_messages(
        chat_id=chat,
        from_chat_id=tg_id.files,
        message_ids=30)


@app.on_message(filters.command("telemetry", prefixes="."))
def telemetry(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat, msg.telemetry)
    app.forward_messages(chat_id=chat,
                         from_chat_id=tg_id.files,
                         message_ids=11)


@app.on_message(filters.chat('me') & filters.video)
def contacts(_, message):
    app.send_message(chat_id='me',
                     text=f'{message.video.file_id}')


@app.on_message(filters.chat(tg_id.files) & filters.video)
def contacts(_, message):
    app.send_message(chat_id=tg_id.files,
                     text=f'{message.video.file_id}, {message.message_id}')


@app.on_message(filters.chat(tg_id.files) & filters.document)
def contacts(_, message):
    app.send_message(chat_id=tg_id.files,
                     text=f'{message.document.file_id}, {message.message_id}')


@app.on_message(filters.chat('me') & filters.document)
def contacts(_, message):
    app.send_message(chat_id='me',
                     text=f'{message.document.file_id}, {message.message_id}')


@app.on_message(filters.regex('.test'))
def funcs(_, message):
    app.restrict_chat_member(chat_id=tg_id.chat_id,
                             user_id=message.from_user.id,
                             permissions=ChatPermissions(),
                             until_date=int(time.time() + 40))


@app.on_message(filters.command("chats", prefixes=".") & filters.me)
def chats(_, message):  # sourcery skip: dict-comprehension, move-assign-in-block
    app.delete_messages(tg_id.chat_id, message.message_id)
    chat = tg_id.chat_id
    people = {}
    total = app.get_chat_members_count(chat)
    for message in app.iter_history(chat, limit=1000):
        if message.from_user and not message.from_user.is_bot:
            people[message.from_user.id] = message.from_user.first_name

    print(len(people) / total)


@app.on_message(filters.regex("22212221") & ~filters.me)
def avtootvet(_, message):
    if message.chat.type not in "private":
        return
    next_id = message.message_id + 1
    app.send_message(chat_id=message.from_user.id, text='Секунду...')
    perc = 0

    while perc < 100:
        try:
            text = "🧭 Идёт поиск файла ..." + str(perc) + "%"
            app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text=text)

            perc += random.randint(3, 6)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text="🟢 Файл найден!")
    sleep(1)

    app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text="🔜 Отправляю файл ...")
    perc = 0

    while perc < 100:
        try:
            text = "🔜 Отправляю файл ..." + str(perc) + "%"
            app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text=text)

            perc += random.randint(1, 5)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    app.edit_message_text(chat_id=message.from_user.id, message_id=next_id, text="🟢 Файл отправлен!")
    app.send_message('me', f'Пользователь скачал файл @{message.from_user.username} {message.from_user.id}')


@app.on_message(filters.voice_chat_started & filters.chat(tg_id.chat_id))
def voice_chat_started(_):
    app.send_message(chat_id=tg_id.chat_id, text='**ВНИМАНИЕ!**\n'
                                                 'Созвон начался.\n'
                                                 'Заходите')


@app.on_message(filters.regex('self-presentation') & filters.me)
def voice_chat_scheduled(_, message):
    chat = message.chat.id
    app.delete_messages(chat, message.message_id)
    app.send_message(chat_id=chat, text=msg.self_presentation)


@app.on_message(filters.regex('vc-scheduled') & filters.chat(tg_id.chat_id) & filters.me)
def voice_chat_scheduled(_, message):
    app.delete_messages(tg_id.chat_id, message.message_id)
    app.send_poll(
        chat_id=tg_id.chat_id,
        question='Внимание, я запланировал аудиозвонок.\n'
                 'Кто будет?',
        options=list(['Точно буду',
                      'Постараюсь быть',
                      'Хочу, но не могу в это время',
                      'Не актуально']),
        is_anonymous=False

    )
    sleep(1)
    app.vote_poll(chat_id=tg_id.chat_id, message_id=message.message_id, options=0)


@app.on_message(filters.voice_chat_ended & filters.chat(tg_id.chat_id))
def voice_chat_started(_, message):
    app.send_message(
        chat_id=tg_id.chat_id,
        text='Созвон завершён.\nВсе, кто был на созвоне - вы молодцы!',
    )

    app.send_poll(
        chat_id=tg_id.chat_id,
        question='Оставьте свою обратную связь по прошедшему созвону...',
        options=list(['Мне понравилось, извлёк для себя пользу, пойду внедрять',
                      'Было интересно, но не понял, как применить для себя (своей ниши)',
                      'Не участвовал в созвоне, не смог в это время',
                      'Не участвовал в созвоне, не актуально']),
        is_anonymous=False

    )
    sleep(2)
    app.vote_poll(chat_id=tg_id.chat_id,
                  message_id=message.message_id,
                  options=0)


# стартовая регистрация пользователя
@app.on_message(filters.new_chat_members & filters.chat(tg_id.chat_id))
def new_chat_members(_, message):
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'

    if not db.subscriber_exists(message.from_user.id):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        app.send_chat_action(chat_id=tg_id.chat_id, action='typing')
        sleep(3)
        app.send_message(chat_id=tg_id.chat_id,
                         text=f'Приветствую тебя, {mention}!\n'
                              f'Добро пожаловать в Акселератор!\n'
                              f'Можешь кратко представиться.\n'
                              f'**Чем ты можешь быть полезен(-на) и с какими вопросами к тебе можно обратиться?**')
    else:
        # если он уже есть, то блокируем и удаляем из чата
        db.update_subscription(message.from_user.id, False)
        app.block_user(user_id=message.from_user.id)
        app.ban_chat_member(chat_id=tg_id.chat_id, user_id=message.from_user.id)
        app.delete_messages(message.chat.id, message.message_id)


@app.on_message(filters.left_chat_member & filters.chat(tg_id.chat_id))
def left_chat_member(_, message):
    app.send_chat_action(chat_id=tg_id.chat_id, action='typing')
    sleep(5)
    app.send_message(
        chat_id=tg_id.chat_id,
        text=f'Пользователю @{message.from_user.username} заблокирован доступ к чату')
    app.block_user(user_id=message.from_user.id)


@app.on_message(filters.chat(tg_id.chat_1))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_1)


@app.on_message(filters.chat(tg_id.chat_2))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_2)


@app.on_message(filters.chat(tg_id.chat_3))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_3)


@app.on_message(filters.chat(tg_id.chat_4))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_4)


@app.on_message(filters.chat(tg_id.chat_5))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_5)


@app.on_message(filters.chat(tg_id.chat_6))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_6)


@app.on_message(filters.chat(tg_id.chat_7))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_7)


@app.on_message(filters.chat(tg_id.chat_8))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_8)


@app.on_message(filters.chat(tg_id.chat_9))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_9)


@app.on_message(filters.chat(tg_id.chat_10))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_10)


@app.on_message(filters.chat(tg_id.chat_11))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_11)


@app.on_message(filters.chat(tg_id.chat_12))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_12)


@app.on_message(filters.chat(tg_id.chat_13))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_13)


@app.on_message(filters.chat(tg_id.chat_14))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_14)


@app.on_message(filters.chat(tg_id.chat_15))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_15)


@app.on_message(filters.chat(tg_id.chat_16))
def left_chat_member(_, message):
    app.read_history(tg_id.chat_16)
