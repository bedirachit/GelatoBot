from rasa.utils.endpoints import EndpointConfig
from rasa.core.agent import Agent
import asyncio
from rasa.core.tracker_store import MongoTrackerStore
from rasa.core.domain import Domain
import logging
from logs import LogHandler
from config import ConfigManager as CM


# setup logging
ErrorLogger = logging.getLogger("ErrorLogs")
InfoLogger = logging.getLogger("InfoLogs")
LogHandler.setup_logging()

domain = Domain.load('domain.yml')
modelPath = CM.rasa_model_path
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

agent = Agent.load(str(modelPath), action_endpoint=action_endpoint, tracker_store=MongoTrackerStore(domain=domain))


async def parse(text, senderId):
    global agent
    response = await agent.handle_text(text,sender_id=senderId)
    return response


def get_bot_response(userMsg, senderId):
    response = None
    if agent.is_ready():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(parse(userMsg, senderId))
        InfoLogger.info("BOT RESPONSE ::: " + str(response))
    return response
