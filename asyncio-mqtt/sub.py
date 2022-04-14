import random
import os.path
import ssl

import asyncio
from asyncio_mqtt import Client

from paho.mqtt import client as mqtt_client
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

broker = 'localhost'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
#client_id = f'python-mqtt-{random.randint(0, 100)}'
client_id = ''
username = 'mosquitto'
password = '8UqU9Z'

async def subscribe(client: mqtt_client):
    async with client.filtered_messages("python/mqtt") as messages:
        await client.subscribe("python/mqtt")
        async for msg in messages:
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            response_topic = msg.properties.ResponseTopic
            print('response topic:%s' % response_topic)


async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(os.path.dirname(__file__) + '/../cert/localhost.crt')

    async with Client(
        hostname=broker,
        port=port,
        client_id=client_id,
        username=username,
        password=password,
        tls_context=ssl_context,
        protocol=mqtt_client.MQTTv5
        ) as client:
        await subscribe(client)

if __name__ == '__main__':
    asyncio.run(main())
