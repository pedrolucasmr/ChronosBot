from datetime import datetime
import pytz

async def time_messages():
    now = datetime.now(pytz.timezone("America/Sao_Paulo"))
    return now.strftime("%H:%M:%S")