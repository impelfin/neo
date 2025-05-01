from slack_sdk import WebClient
import os.path
import json

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

class SlackAPI:
    def __init__(self, token):
        self.client = WebClient(token)

    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        channels = result.data['channels']
        channel = list(filter(lambda c: c['name'] == channel_name, channels))[0]
        channel_id = channel["id"]
        return channel_id

    def get_message_ts(self, channel_id, query):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data['messages']
        filtered_messages = list(filter(lambda m: m['text'] == query, messages))
        if not filtered_messages:
            result = self.post_message(channel_id, query)
            return result['ts']

    def post_thread_message(self, channel_id, message_ts, text):
        result = self.client.chat_postMessage(
            channel = channel_id,
            text = text,
            thread_ts = message_ts
        )
        return result
    
    def post_message(self, channel_id, text):
        result = self.client.chat_postMessage(
            channel = channel_id,
            text = text
        )
        return result

BotToken = get_secret("slack_BotOAuthToken")
slack = SlackAPI(BotToken)
channel_name = "project"
query = "slackbot test"
text = "Hello, I'm Slack Bot.."

channel_id = slack.get_channel_id(channel_name)
message_ts = slack.get_message_ts(channel_id, query)
slack.post_thread_message(channel_id, message_ts, text)