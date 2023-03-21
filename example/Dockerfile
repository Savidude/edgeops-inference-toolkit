FROM python:3.8-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENV MODEL_NAME="gbdt_model.pkl"
ENV MODELS_DIR="./models"
ENV MQTT_INPUT_TOPIC="inference/sample/scania/aps/req"
ENV MQTT_OUTPUT_TOPIC="inference/sample/scania/aps/res"

CMD [ "python3", "executor.py"]
