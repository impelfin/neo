import requests
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse
import json
import os.path

app = FastAPI ( )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

UserToken = get_secret("slack_UserOAuthToken")
BotToken = get_secret("slack_BotOAuthToken")
channelName = "#project"

@app.get(path='/')
async def health_check():
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

@app.post(path='/sendUserchat')
async def sendUserChat(text:str):
    post_message(UserToken,channelName,text)
    return {f'message:{text}'} 

@app.post(path='/sendBotchat')
async def sendBotChat(text:str):
    post_message(BotToken,channelName,text)
    return {f'message:{text}'} 

@app.post(path='/sendhook')
async def sendHook(text:str):
    webhookToken = get_secret("slack_WebHookToken")
    cmd = "curl -X POST -H " 
    cmd += "'Content-type: application/json' --data "
    cmd += "'{" + '"text"' + ":" + '"' + text + '"' + "}' "
    cmd += webhookToken    
    os.system(cmd)
    return cmd 