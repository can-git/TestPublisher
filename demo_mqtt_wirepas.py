import paho.mqtt.client as mqtt

broker = "172.16.138.201"
port = 1883
topic = "#"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe(topic, qos=1)
    else:
        print("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    arr = str(msg.payload).split('\\x')
    print(msg.topic)

    print(msg.payload)


client = mqtt.Client()
client.username_pw_set(username="mqttmasteruser", password="gFbgSPBx40s9M1gMUMPt3uZ3twQ")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)
client.loop_forever()
