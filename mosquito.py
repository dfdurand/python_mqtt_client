import paho.mqtt.client as mqtt
import time
import random

#broker_address= "127.0.0.1"
broker_address= "test.mosquitto.org"
#broker_address="iot.eclipse.org"


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

client = mqtt.Client("user")  # nouvelle instance


client.connect(broker_address)  # connexion au broker
print("connexion au broker")

client.on_message = on_message  # appel de la fonction retour
#x = random.randint(0, 100)
x = 105
print("subscription au topic: ", "home/temp²")
client.subscribe("home/temp")
print("publlication sur le topic: ","home/temp")
client.publish("home/temp",x)


client.loop_forever()

