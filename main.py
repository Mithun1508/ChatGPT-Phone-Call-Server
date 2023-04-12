# See README.md for instructions on how to get started
from fastapi import Response
import os
import vocode
from vocode.streaming.telephony.inbound_call_server import InboundCallServer
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.models.telephony import TwilioConfig
from vocode.streaming.models.agent import ChatGPTAgentConfig

vocode.api_key = os.getenv("VOCODE_API_KEY")

REPLIT_URL = f"https://{os.getenv('REPL_SLUG')}.{os.getenv('REPL_OWNER')}.repl.co"

if __name__ == "__main__":
  server = InboundCallServer(
    agent_config=ChatGPTAgentConfig(
      initial_message=BaseMessage(text="Hey Zahid! What's up?"),
      prompt_preamble=
      "You are a helpful AI assistant. Answer questions in 50 words or less.",
    ),
    twilio_config=TwilioConfig(
      account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
      auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
    ),
  )
  server.app.get("/")(lambda: Response(
    content=
    f"<div>Fork this Repl and see README.md for instructions! Don't forget to paste your Repl's URL into your Twilio config like this: {REPLIT_URL}/vocode<br><br>Watch the <a href='https://twitter.com/chillzaza_/status/1641255992045322240?s=20' target='_blank'>live demo</a> to see it in action!</div>",
    media_type="text/html"))
  server.run(host="0.0.0.0", port=3000)
