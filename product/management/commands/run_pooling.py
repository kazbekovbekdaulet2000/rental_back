from telegram import Bot, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext
)
from product.models.bot import BotUser
from rental_back.settings import TELEGRAM_TOKEN


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = BotUser.objects.update_or_create(user_id=update.message.chat_id, defaults=dict(name=update.message.chat.username, approved=False))
    if(created):
        update.message.reply_text(text=f"{u.name}, Вам будут приходить уведомления во время заказов на сайте")


def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", command_start))

    bot_info = Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")

    updater.start_polling()
    updater.idle()
