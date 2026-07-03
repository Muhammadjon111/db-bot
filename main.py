# Bismillahir Rohmanir Rohiim

from telegram.ext import Updater, CommandHandler,MessageHandler,CallbackQueryHandler,Filters
from send_buttons import send_main_menu
from inlines import inline_handler
from messages import message_handler
from config import TOKEN

def start_handler(update,context):
    send_main_menu(context=context,
                   chat_id=update.message.from_user.id)

def main():
    print("TOKEN =", TOKEN)
    updater=Updater(TOKEN)
    dispatcher=updater.dispatcher

    dispatcher.add_handler(CommandHandler('start',start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text,message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))



    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
# from send_buttons.send_menu import send_main_menu
# from inlines import inline_handler
# from messages import message_handler
# from config import TOKEN
#
#
# def start_handler(update, context):
#     send_main_menu(context=context, chat_id=update.message.from_user.id)
#
#
# def main():
#     updater=Updater(TOKEN)
#     dispatcher=updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler('start',start_handler))
#     dispatcher.add_handler(MessageHandler(Filters.text,message_handler))
#     dispatcher.add_handler(CallbackQueryHandler(inline_handler))
#
#     updater.start_polling()
#     updater.idle()
#
#
# if __name__ == '__main__':
#     main()
#
