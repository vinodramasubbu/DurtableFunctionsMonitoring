# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from datetime import timedelta
import logging
import json

import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    
    # Monitoring
    expiry_time = context.current_utc_datetime + timedelta(minutes=5)
    while context.current_utc_datetime < expiry_time:
        result1 = yield context.call_activity('CheckWeather', "xxx")
        if float(result1) > 21 and float(result1) < 35:   
            print(result1)
            status = f"The weather is clear outside! Go for a walk !"
            print(status)
            yield context.call_activity("SendSMS", status)
            break
        else:
            # Reporting the status
            status = f"The weather is not good for a walk, I will continue monitoring and let you know when its good ..."
            context.set_custom_status(status)
            yield context.call_activity("SendSMS", status)
            # Schedule a new "wake up" signal
            next_check = context.current_utc_datetime + timedelta(minutes=1)
            yield context.create_timer(next_check)
            print({status})
    return "Monitor completed!"

main = df.Orchestrator.create(orchestrator_function)