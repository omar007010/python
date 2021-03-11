import telegram
from common import config
import time

bot = telegram.Bot(token=config.token)
print(config.token)
bot.send_message(chat_id="-1001454749465", text="测试消息")

