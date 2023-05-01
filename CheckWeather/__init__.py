# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import requests
import azure.functions as func
import json

def main(name: str) -> str:
    url = 'https://api.open-meteo.com/v1/forecast?latitude=35.76&longitude=-78.91&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m'
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    #temperature = json.dumps(response["current_weather"])
    #print(temperature)

    if response.status_code == 200:
        data = response.json()
        print(data["current_weather"]["temperature"])
        data1 = data["current_weather"]["temperature"]
    else:
        print('Error!')

    return f"{data1}"
