import  paho mqtt.client as mqtt
import keyboard  

BROKER_ADDRESS = "your_broker_address"
BROKER_PORT = 1883
TOPIC = "bluetooth_speaker"

def handle_bluetooth_command(command):
    key_map = {
        "play": "play/pause media",
        "pause": "play/pause media",
        "next": "next track",
        "previous": "previous track"
    }

    if command in key_map:
        try:
            keyboard.send(key_map[command])
            print(f"Executed Bluetooth command: {command}")
        except Exception as e:
            print(f"Failed to send command '{command}': {e}")
    else:
        print(f"Unknown command: {command}")

def on_message(client, userdata, message):
    command = message.payload.decode().strip().lower()
    handle_bluetooth_command(command)

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER_ADDRESS, BROKER_PORT)
client.subscribe(TOPIC)

print("MQTT client is running. Waiting for commands...")
client.loop_forever()
