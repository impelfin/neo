import requests
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse
import json
import os.path

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errMsg = "Set the {} environment variable.".format(setting)
        return errMsg
    
UserToken = get_secret("slack_UserOAuthToken")
BotToken = get_secret("slack_BotOAuthToken")