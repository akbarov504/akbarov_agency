from pathlib import Path
from aiogram import Bot, Dispatcher

STATE_FILE_PATH = Path(__file__).parent.parent.joinpath("states").joinpath("state.json")

token = "7452726088:AAHOK986b29PE3b18Dqdh12zOYeC3_m0AkA"
bot = Bot(token)
dp = Dispatcher(bot)
