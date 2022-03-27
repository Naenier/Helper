import sqlite3


class user_database:
    """Управление БД"""
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status=True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def subscriber_username(self, username):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `username` = ?", (username,)).fetchall()
            return bool(len(result))

    def subscriber_name(self, name):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `name` = ?", (name,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, username, firstname, lastname, status=True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, 'username', 'firstname', 'lastname', `status`) VALUES(?,?,?,?)", (user_id, username, firstname, lastname, status))

    def update_subscription(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def update_username(self, user_id, username):
        """Обновляем никнейм"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `username` = ? WHERE `user_id` = ?", (username, user_id))

    def update_firstname(self, user_id, firstname):
        """Обновляем имя"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `firstname` = ? WHERE `user_id` = ?", (firstname, user_id))

    def update_lastname(self, user_id, lastname):
        """Обновляем фамилию"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `lastname` = ? WHERE `user_id` = ?", (lastname, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
