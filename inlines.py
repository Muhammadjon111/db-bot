#  Bismillahir Rohmanir Rohiim

from send_buttons import send_regions, send_countries
from database import Database
db=Database("database-sample.db")

def inline_handler(update,context):
    print("inline button clicked")
    query=update.callback_query
    print(f"callback data: {query.data}")
    data_sp=str(query.data).split("_")
    print(f"data_sp: {data_sp}")
    print(f"data_sp[0]: {data_sp[0]}")
    if data_sp[0]=="region":
        print("clicked region block")
        if data_sp[1].isdigit():
            print("data_sp[1] is a digit")
            countries=db.get_countries_by_region(int(data_sp[1]))
            print(f"countries: {countries}")
            send_countries(context=context,
                           countries=countries,
                           chat_id=query.message.chat_id,
                           message_id=query.message.message_id)

        elif data_sp[1]=='back':
            print("entered back block")
            regions=db.get_all_regions()
            print(f"regions: {regions}")
            send_regions(context=context,
                         regions=regions,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id)

    if data_sp[0]=="country":
        pass
    if data_sp[0]=='close':
        msg=query.message.edit_text(
            text="🕓",
            reply_markup=None,
        )
        context.bot.delete_message(chat_id=query.message.chat_id,
                                   message_id=msg.message_id)
