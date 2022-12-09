import loguru

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.database.methods.update import *
from bot.database.methods.get import *

from bot.keyboards import *

class IsAdmin:
    def ValAdmin(self, message: Message, Id):
        person = message.from_user.id
        for x in Id:
            if person == x[0]:
                return 'Admin'
        return 'User'
Admin = IsAdmin()
