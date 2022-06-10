import paho.mqtt.client as mqtt
from datetime import date, datetime
import serial
import time


broker_address= "127.0.0.1"  #test.mosquitto.org

#recupération de la date et l'heure

#temps
now = datetime.now()
ctime = now.strftime("%H:%M:%S")

#date
day = date.today()
nday = day.strftime("%d-%m-%Y")


#création  communication arduino

port = 'COM9'
try:
    arduino = serial.Serial(port, 115200, timeout=1)
except Exception:
    print(" problème de connexion serie ")


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


client = mqtt.Client("user") #nouvelle instance
#print("connecting to broker")
client.connect(broker_address) #connexion au broker
client.on_message=on_message #fonction retour
print("connexion au broker")


while True:
    data = arduino.readline()
    print(data.decode('utf'))
    print("Publication du message au topic ", "db/data , db/date et db/hour")
    client.publish("db/data", data.decode('utf'))
    client.publish("db/hour", ctime)
    client.publish("db/date", nday)
    time.sleep(5)