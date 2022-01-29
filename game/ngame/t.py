from telethon import TelegramClient, client, events
from telethon.sync import TelegramClient
import asyncio
import json

api_id = 7569661
api_hash = "2b19023078dacc6aca30da8ec675e7d9"


class Client(TelegramClient):
    def __init__(self, api_id: int, api_hash: str, channel_name: set, channel_link: str):
        self.session_name = "session"
        self.api_id = api_id
        self.api_hash = api_hash
        super().__init__(
            self.session_name,
            self.api_id, api_hash
        )
        self.channel_name = channel_name
        self.channel_link = channel_link

        super().start()


class InputException(Exception):
    def __init__(self, info):
        self.info = info


def check_datas(filename):
    with open(filename, "r") as file_:
        datas = json.load(file_)

        if ( datas.get("channel_name") is None or datas.get("channel_link") is None ):
            raise InputException("Не корректные данные > {}  (Одно из значений None)".format(filename))
        if ( len(datas.get("channel_name")) == 0 or len(datas.get("channel_link")) == 0 ):
            raise InputException("Не корректные данные > {}  (Одно из значений не введено)".format(filename))

        return (0, datas.get("channel_name"), datas.get("channel_link"))



if __name__ == "__main__":
    temp_D = check_datas("datas.json")
    if temp_D[0] == 0:

        client = Client(api_id, api_hash, temp_D[1], temp_D[2])

        @client.on(events.NewMessage(chats = (client.channel_name)))
        async def handler(event):
            channel = await client.get_entity(client.channel_link)

            await client.send_message(channel, event.message)

        client.run_until_disconnected()