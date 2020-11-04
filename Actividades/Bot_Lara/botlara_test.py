import slack
import os
from slack import WebClient
from bot_lara import Bot_Lara


# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new coinbot
bot_lara = Bot_Lara("#Alumno_SebastianLara")

# Get the onboarding message payload
message = bot_lara.get_message_payload()

# Post the onboarding message in slack
slack_web_client.chat_postMessage(**message)