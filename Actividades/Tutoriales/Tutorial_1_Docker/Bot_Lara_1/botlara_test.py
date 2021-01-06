from slack import WebClient
from bot_lara import Bot_Lara
import os
import slack
# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
bot_lara = Bot_Lara("#playground")

# Get the onboarding message payload
message = bot_lara.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)