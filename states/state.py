from json import dumps, loads
from configs.config import STATE_FILE_PATH

class State:
    def __init__(self, state: str, data: dict, chat_id: int) -> None:
        self.__state = state
        self.__data = data
        self.__chat_id = chat_id
    
    def get_state(self) -> str:
        return self.__state
    
    def get_data(self) -> dict:
        return self.__data
    
    def get_chat_id(self) -> int:
        return self.__chat_id

def to_dict(state: State) -> dict:
    _state = {
        "chat_id": state.get_chat_id(),
        "data": state.get_data(),
        "state": state.get_state()
    }
    return _state

def read() -> list:
    with open(STATE_FILE_PATH, "rt") as file:
        return loads(file.read())

def append(state: State) -> None:
    states = read()
    to_dict_state = to_dict(state)
    for x in states:
        if x.get('chat_id') == to_dict_state.get('chat_id'):
            states.remove(x)
            break
    states.append(to_dict_state)
    with open(STATE_FILE_PATH, "wt") as file:
        file.write(dumps(states))
        return None

def get_state(chat_id: int) -> str:
    states = read()
    for state in states:
        if state.get("chat_id") == chat_id:
            return state.get("state")

def get_data(chat_id: int) -> dict:
    states = read()
    for state in states:
        if state.get("chat_id") == chat_id:
            data = state.get("data")
            return data
