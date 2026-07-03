# Bismillahir Rohmanir Rohiim

from send_buttons.send_regions import send_regions
from config import DATA_BASE
from database import Database

db=Database(DATA_BASE)


def message_handler(update,context):
    message=update.message.text
    if message=="regions":
        regions=db.get_all_regions()
        send_regions(context=context,regions=regions,chat_id=update.message.from_user.id)
