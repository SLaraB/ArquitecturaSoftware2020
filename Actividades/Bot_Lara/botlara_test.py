import slack
import os
from slack import WebClient
from botlara import Bot_Lara


# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new coinbot
Bot_Lara = Bot_Lara("#playground")

# Get the onboarding message payload
message = Bot_Lara.get_message_payload()

# Post the onboarding message in slack
slack_web_client.chat_postMessage(**message)