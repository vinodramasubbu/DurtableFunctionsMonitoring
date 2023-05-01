# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from azure.communication.sms import SmsClient
#from azure.identity import DefaultAzureCredential
#from azure.communication.sms import SendSmsOptions

def main(name: str) -> str:
    connection_string = "endpoint=https://xxxxxx.communication.azure.com/;accesskey=xxxxxxxxxxx"
    sms_client = SmsClient.from_connection_string(connection_string)

    # To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have
    # AZURE_TENANT_ID, AZURE_CLIENT_ID and AZURE_CLIENT_SECRET as env variables.
    #endpoint = "https://xxxxx.communication.azure.com/"
    #sms_client = SmsClient(endpoint, DefaultAzureCredential())
    sms_responses = sms_client.send(
    from_="+1xxxxxxxxxx",
    to="+1xxxxxxxxxx",
    message=name)
    #enable_delivery_report=True, # optional property
    #tag="custom-tag") # optional property

    return f"{name}"
