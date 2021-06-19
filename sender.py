import asyncio
import sqlite3
from email.message import EmailMessage
import aiosmtplib

message = EmailMessage()


def get_users_data():
    with sqlite3.connect('contacts.db') as connect:
        cursor = connect.cursor()
        cursor.execute("""SELECT first_name, last_name, email FROM contacts""")
        data = cursor.fetchall()
        return data


async def sender(messenger, data):
    for name, lastname, email in data:
        messenger["From"] = "root@localhost"
        messenger["To"] = email
        messenger["Subject"] = f'"Уважаемый {name} {lastname}! ' \
                               f'Спасибо, что пользуетесь нашим сервисом объявлений."'
        await aiosmtplib.send(
            messenger,
            hostname="smtp.yandex.ru",
            port=465,
            username="skitol@yandex.ru",
            password="qxgymlbzrzaypdlt"
        )


async def main():
    await sender(message, get_users_data())


if __name__ == '__main__':
    asyncio.run(main())

