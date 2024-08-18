from aiogram.types import Message
from states.state import get_state, get_data
from aiogram.dispatcher.filters import Filter

class CheckState(Filter):
    def __init__(self, state: str) -> None:
        super().__init__()
        self.state = state
    
    async def check(self, message: Message) -> bool:
        state = get_state(message.chat.id)
        if self.state == state:
            return True
        return False
