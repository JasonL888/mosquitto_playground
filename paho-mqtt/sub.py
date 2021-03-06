import random
import os.path

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


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT Broker!")
            if properties != None:
                print('properties:%s' % properties.__dict__)
                print('AssignedClientIdentifier:%s' % properties.AssignedClientIdentifier)

        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id, protocol=mqtt_client.MQTTv5)
    client.tls_set(os.path.dirname(__file__) + '/../cert/localhost.crt')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    props = Properties(PacketTypes.CONNECT)
    props.RequestResponseInformation=1
    props.UserProperty = ("usp-endpoint-id","yyy-endpoint-id")
    client.connect(broker, port, properties=props)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        response_topic = msg.properties.ResponseTopic
        print('response topic:%s' % response_topic)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
