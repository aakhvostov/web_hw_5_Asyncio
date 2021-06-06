import asyncio
import sqlite3
from email.message import EmailMessage

import aiosmtplib


def get_users_data():
    with sqlite3.connect('contacts.db') as connect:
        cursor = connect.cursor()
        cursor.execute("""SELECT first_name, last_name, email FROM contacts""")
        data = cursor.fetchall()
        return data


async def sender(data):
    message = EmailMessage()
    message["From"] = "root@localhost"
    for person in data:
        message["To"] = person[2]
        message["Subject"] = f'"Уважаемый {person[0]} {person[1]}! ' \
                             f'Спасибо, что пользуетесь нашим сервисом объявлений."'
        await aiosmtplib.send(message, hostname="127.0.0.1", port=25)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.run(sender(get_users_data()))
