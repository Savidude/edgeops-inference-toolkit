FROM python:3.8-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENV MODEL_NAME="<MODEL_FILE_NAME>"
ENV MODELS_DIR="<MODEL_DIR>"
ENV MQTT_INPUT_TOPIC="<MQTT_INPUT_TOPIC>"
ENV MQTT_OUTPUT_TOPIC="<MQTT_OUTPUT_TOPIC>"

CMD [ "python3", "executor.py"]
