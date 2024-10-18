import json
import random
import time
import paho.mqtt.client as mqtt

broker = "172.16.138.15"
port = 1883
# topic = "tb/cluster/sensors/SN-001/temperature"
topic = "v1/devices/me/telemetry"

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client()
client.username_pw_set(username="a", password="b")
client.on_connect = on_connect
client.connect(broker, port)

client.loop_start()  # Non-blocking loop

while True:
    message = {"value": str(random.random())}
    client.publish(topic, json.dumps(message), qos=1)
    time.sleep(1)  # Publish every 1 second
