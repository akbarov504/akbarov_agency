from aiogram import executor
from configs.config import dp

if __name__ == "__main__":
    from handlers import handler
    executor.start_polling(dp, skip_updates=True)
