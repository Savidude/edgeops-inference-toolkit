import os
import time

import random
import string

import inference_handler as handler

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "host.docker.internal"
MODEL_NAME = os.environ.get("MODEL_NAME")
MODEL_DIR = models_dir=os.environ.get("MODELS_DIR")
INPUT_TOPIC = os.environ.get("MQTT_INPUT_TOPIC")
OUTPUT_TOPIC = os.environ.get("MQTT_OUTPUT_TOPIC")

model = handler.load_model(models_dir=MODEL_DIR, model_name=MODEL_NAME)

def publish_output(client, message):
    client.publish(OUTPUT_TOPIC, message)

def on_message(client, userdata, message):
    input_data = handler.preprocess_input(input_data=str(message.payload.decode("utf-8")), models_dir=MODEL_DIR)
    inference_results = handler.infer(model=model, input_data=input_data)
    output = handler.output(inference_result=inference_results)
    publish_output(client, output)

def main():
    model_id = ''.join(random.choice(string.ascii_lowercase) for i in range(4))

    print(f"Starting MQTT client {model_id}...")
    client = mqtt.Client(f"model-{model_id}")
    client.on_message=on_message

    print("Connecting to local MQTT broker...")
    client.connect(BROKER_ADDRESS)
    client.subscribe(INPUT_TOPIC)
    print(f"Connected! Ready to receive requests from topic {INPUT_TOPIC}")
    client.loop_forever()

if __name__ == '__main__':
	main()
