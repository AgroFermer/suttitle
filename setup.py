import contextlib
import asyncio 
from aiogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, F
import logging


BOT_TOKEN = '6049881080:AAHKRq_ZY7EM7X3Xi-ksFpXSjpCBFp_zf58' 
CHANNEL_ID = -1001747962402
ADMIN_ID = 800995199
async def approve_request (chat_join: ChatJoinRequest, bot: Bot):
   msg= f"Ваша заявка одобрена!\n\nВступить в канал: https://t.me/+dy29ef4hzbhmMDIy"
   button = InlineKeyboardButton(text='ВСТУПИТЬ', url='https://t.me/+dy29ef4hzbhmMDIy', disable_web_page_preview=True)   
   markup = InlineKeyboardMarkup(inline_keyboard=[[button]])


   await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=markup, disable_web_page_preview=True)
 

async def start():
    logging.basicConfig(level=logging.DEBUG,
                           format="%(asctime)s - [%(levelname)s] - %(name)s -"
                           "(%(filename)s.%(funcName)s(%(lineo)d) - %(message)s"
                        )
    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher ()
    dp.chat_join_request.register (approve_request, F.chat.id ==CHANNEL_ID)

    try:
     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
     logging.error( exc_info=True)
    finally:
     await bot.session.close()
       # final


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())

  

