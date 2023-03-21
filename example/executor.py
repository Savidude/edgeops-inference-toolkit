import os
import time

import inference_handler as handler

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "host.docker.internal"

model = handler.load_model(models_dir=os.environ.get("MODELS_DIR"), model_name=os.environ.get("MODEL_NAME"))

def publish_output(client, message):
    client.publish(os.environ.get("MQTT_OUTPUT_TOPIC"), message)

def on_message(client, userdata, message):
    input_data = handler.preprocess_input(input_data=str(message.payload.decode("utf-8")), models_dir=os.environ.get("MODELS_DIR"))
    inference_results = handler.infer(model=model, input_data=input_data)
    output = handler.output(inference_result=inference_results)
    publish_output(client, output)
    print(output)

def main():    
    client = mqtt.Client("model")
    client.on_message=on_message 
    client.connect(BROKER_ADDRESS)
    client.subscribe(os.environ.get("MQTT_INPUT_TOPIC"))
    client.loop_forever()

if __name__ == '__main__':
	main()
