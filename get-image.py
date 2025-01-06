from paho.mqtt import client as mqtt_client
import json
import requests
import os

broker = 'homeassistant.home'
port = 1883
username = 'mqtt_user'
password = 'mqtt_user'
#topic = "double-take/cameras/farstun"
topic_sub = "double-take/cameras/farstun"
client_id = 'xzcfghjt123'
api_url_prefix = 'http://truenas.home:3001/api/storage/matches/'
api_url_suffix = '?box=true'

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
        y = json.loads(msg.payload.decode())
        print(f"Recieved from topic '{msg.topic}' \n")
        #print(json.dumps(y, indent=4))
        #print("\n \n")

        if not len(y["matches"]) == 0:
            with open("/home/llego/farstuns-ansikte/matches", "w") as f:
                f.write("")
            for match in y["matches"]:
                facename = match["name"]
                confidence = match["confidence"]
                filename = match["filename"]
                print(facename + ", " + u"{}%".format(confidence) + ", " + filename)
                with open("/home/llego/farstuns-ansikte/matches", "a") as f:
                    f.write(facename + ": " + u"{}%".format(confidence) + "\n")

            url = api_url_prefix + filename + api_url_suffix
            r = requests.get(url, allow_redirects=True)
            open("/home/llego/farstuns-ansikte/receive.jpg", 'wb').write(r.content)

    client.subscribe(topic_sub)
    client.on_message = on_message

def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    
if __name__ == '__main__':
    main()
