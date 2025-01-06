from paho.mqtt import client as mqtt_client
import subprocess
import time

broker = 'homeassistant.home'
port = 1883
username = 'mqtt_user'
password = 'mqtt_user'
topic = "frigate/farstun/person/snapshot"
topic_sub = "frigate/farstun/person/snapshot"
client_id = 'xzcfghjt123'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        f = open('images/receive.jpg', 'wb')
        f.write(msg.payload)
        f.close()
        print ('image received')

    client.subscribe(topic_sub)
    client.on_message = on_message

def main():
    client = connect_mqtt()
    subscribe(client)
    
    #subprocess.run("sh /home/llego/farstuns-ansikte/refresh_screen.sh", shell=True)
    
    print("Starting new loop")
    client.loop_forever()
    
if __name__ == '__main__':
    main()
